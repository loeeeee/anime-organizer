import os
import sys
import yaml
import re
from typing import Literal, Union
import random
import string
import json

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created successfully.")
        except OSError as e:
            print(f"Error creating folder '{folder_path}': {e}")
    else:
        print(f"Folder '{folder_path}' already exists.")


class Extension:
    VideoExtension = {
        "mp4",
        "mkv",
        "mov",
        "avi",
        "webm",
        "ts",
        "ogg"
    }
    SubtitleExtension = {
        "ass",
        "ssa",
        "srt",
        "vtt",
        "pgssub",
        "vobsub"
    }


class FilterKeywords:
    main_file_path = os.path.dirname(os.path.realpath(__file__))

    filter_words_path = f"{main_file_path}/filter_words.yaml"
    with open(filter_words_path, "r", encoding="utf-8") as f:
        filter_words = yaml.safe_load(f)
    print(filter_words)

    # Meat
    CCGroup = filter_words["CC Group"]
    MediaMeta = filter_words["Media Meta"]
    NoInterest = filter_words["No Interest"]


class SeriesShouldBeDir(Exception):
    pass


class Series:
    def __init__(self, full_path: str):
        self.location = full_path
        print(f"Current working_dir: {full_path}")
        if not os.path.isdir(self.location):
            raise SeriesShouldBeDir
            return
        
        self.seasons = {}
        """Store the season level
        {
            "1": _Season,
            "2": _Season,
            "OAD": _Season,
            "OVA": _Season
        }
        """
        self.name = Series.clean_series_name(full_path)
        print(self.name)
        self.file_system = [(root, dirs, files) for root, dirs, files in os.walk(full_path)]
        self._remove_non_digestable_from_fs()
        # Create Season Map
        self.season_map = SeasonMap(self.file_system)
        
        # Create Episode Map
        self.episode_map = EpisodeMap(self.file_system)

        for season in self.season_map.all_seasons():
            self.seasons[season] = _Season()

        for episode_or_subtitle in self.episode_map:
            season_number = self.season_map[episode_or_subtitle]
            episode_number = self.episode_map[episode_or_subtitle]

            if Series.judge_file_type(episode_or_subtitle) == "video":
                media = _Epsiode(episode_or_subtitle)
                self.seasons[season_number][episode_number] = media
            elif Series.judge_file_type(episode_or_subtitle) == "subtitle":
                pass
            else:
                print(f"Bad file, {episode_or_subtitle}")
                continue

        for episode_or_subtitle in self.episode_map:
            season_number = self.season_map[episode_or_subtitle]
            episode_number = self.episode_map[episode_or_subtitle]

            if Series.judge_file_type(episode_or_subtitle) == "subtitle":
                media = _Subtitle(episode_or_subtitle)
                try:
                    self.seasons[season_number][episode_number].subtitles["chi"] = media
                except KeyError:
                    continue
            elif Series.judge_file_type(episode_or_subtitle) == "video":
                pass
            else:
                print(f"Bad file, {episode_or_subtitle}")
                continue
        
    def display(self) -> None:
        print(f"|--{self.name}")
        for season in self.seasons:
            print(f"|----Season {season}")
            focused_season = self.seasons[season]
            for episode in focused_season:
                og_path = focused_season[episode].location
                abbr_og_path = os.path.basename(og_path)
                print(f"|------S{str(season).zfill(2)}E{str(episode).zfill(2)}.tv[{abbr_og_path}]")
                subtitles = focused_season[episode].subtitles
                for language in subtitles:
                    og_path = subtitles[language].location
                    abbr_og_path = os.path.basename(og_path)
                    print(f"|------S{str(season).zfill(2)}E{str(episode).zfill(2)}.{language}.sub[{abbr_og_path}]")

    def link(self, target_dir: str) -> None:
        working_dir = os.path.join(target_dir, self.name)
        Series.create_folder_if_not_exists(working_dir)
        for season in self.seasons:
            season_path = os.path.join(working_dir, f"Season_{season}")
            Series.create_folder_if_not_exists(season_path)
            focused_season = self.seasons[season]
            for episode in focused_season:
                og_path = focused_season[episode].location
                extention_name = Series.get_file_extention_name(og_path)
                episode_path = os.path.join(season_path, f"S{str(season).zfill(2)}E{str(episode).zfill(2)}{extention_name}")
                try:
                    os.symlink(og_path, episode_path)
                except FileExistsError:
                    print(f"{episode_path} already has something there")

                subtitles = focused_season[episode].subtitles
                for language in subtitles:
                    og_path = subtitles[language].location
                    extention_name = Series.get_file_extention_name(og_path)
                    subtitle_path = os.path.join(season_path, f"S{str(season).zfill(2)}E{str(episode).zfill(2)}.{language}{extention_name}")
                    try:
                        os.symlink(og_path, subtitle_path)
                    except FileExistsError:
                        print(f"{episode_path} already has something there")

    def dumps(self) -> dict:
        mapping = {}
        for season in self.seasons:
            mapping[season] = {}

            focused_season = self.seasons[season]
            for episode in focused_season:
                og_path = focused_season[episode].location
                mapping[season][episode] = {"media": og_path, "subtitles": {}}

                subtitles = focused_season[episode].subtitles
                for language in subtitles:
                    og_path = subtitles[language].location
                    mapping[season][episode]["subtitles"][language] = og_path

        return mapping


    def _remove_non_digestable_from_fs(self) -> None:
        clean_fs = []
        dirty_pathes = []
        for root, dirs, files in self.file_system:
            # Init
            _clean_dirs = []
            _dirty_dirs = []
            _clean_files = []

            # Select dirs
            for _dir in dirs:
                if not Series.isNoInterest(_dir):
                    _clean_dirs.append(_dir)
                else:
                    _dirty_dirs.append(os.path.join(root, _dir))

            # Select files
            for _file in files:
                if not Series.isNoInterest(_file) and not Series.judge_file_type(_file) is None:
                    _clean_files.append(_file)
                else:
                    pass
            clean_fs.append(
                (root, _clean_dirs, _clean_files)
            )
            dirty_pathes.extend(_dirty_dirs)
        #print(json.dumps(clean_fs, indent=2))
        #print()
        # Remove children of null parent node
        resilvered_fs = []
        for root, dirs, files in clean_fs:
            isHanging = False
            for dirty_path in dirty_pathes:
                if root.startswith(dirty_path):
                    isHanging = True
            if not isHanging:
                resilvered_fs.append(
                    (root, dirs, files)
                )

        self.file_system = resilvered_fs
    
    def __str__(self):
        return self.name
        
    @staticmethod
    def isNoInterest(file_dir_name: str) -> bool:
        result = False

        # No Interest
        filter_construct_middleware = [f"{i}".replace(".", "\.").replace("-", "\-") for i in FilterKeywords.NoInterest]
        combined = rf"[\b\_\-\.\[\(\s](?:{'|'.join(filter_construct_middleware)})[s\d]*[\b\_\-\.\]\)\s]"
        reg = re.compile(rf"{combined}", flags=re.IGNORECASE)
        if re.findall(reg, file_dir_name):
            result = True

        combined = rf"(?:{'|'.join(filter_construct_middleware)})[s\d]*"
        reg = re.compile(rf"{combined}", flags=re.IGNORECASE)
        if re.findall(reg, file_dir_name):
            result = True
        return result

    @staticmethod
    def judge_file_type(name: str) -> Literal["video", "subtitle", None]:
        """Judge file type based on extension

        Args:
            name (str): file name to be judged

        Returns:
            str: only return certain strings
        """
        _, ext = os.path.splitext(name)
        ext = ext.lower()[1:]
        if ext in Extension.VideoExtension:
            # comment: Find videos 
            return "video"
        elif ext in Extension.SubtitleExtension:
            # comment: Find subtitles
            return "subtitle"
        # end if
        return None
    
    @staticmethod
    def clean_name(name: str) -> str:
        # Parse
        [name, extension] = os.path.splitext(name)

        # Remove CC Group name
        filter_construct_middleware = [f"({i})" for i in FilterKeywords.CCGroup]
        combined = "|".join(filter_construct_middleware).replace(".", "\.").replace("-", "\-")
        reg = re.compile(rf"{combined}(&{combined})*?", flags=re.IGNORECASE)

        name = re.sub(reg, "", name)

        # Remove meta
        filter_construct_middleware = [f"({i})" for i in FilterKeywords.MediaMeta]
        combined = "|".join(filter_construct_middleware).replace(".", "\.").replace("-", "\-")
        reg = re.compile(rf"{combined}", flags=re.IGNORECASE)
        name = re.sub(reg, "%ReM0vE%", name)

        # Remove REMOVE tag
        #reg = r"\[([^\]]*?[(%ReM0vE%)]+[^\[]*?)+?\]"
        reg = r"\[[^\]]*?(%ReM0vE%)[^\[]*?\]"
        name = re.sub(reg, "", name)

        # Remove [Weired characters]
        reg = r"\[\W*?\]"
        name = re.sub(reg, "", name)

        # Clean up
        reg = r"\[[(\s)-]*\]" # Remove [ ], []
        name = re.sub(reg, "", name).strip()
        return f"{name}{extension}"

    @staticmethod
    def clean_series_name(full_path: str) -> str:
        basename = os.path.basename(os.path.normpath(full_path))
        clean_name = Series.clean_name(basename)

        # Change . into space
        reg = r'\.'
        clean_name = re.sub(reg, " ", clean_name)

        # Remove year
        clean_name = Series.remove_year_number(clean_name)

        # Remove season info
        reg = r'(?:Season|S)[\s]*?(\d{1,2})'
        reg = re.compile(reg, flags=re.IGNORECASE)
        clean_name = re.sub(reg, " ", clean_name)

        # Remove remove padding
        reg = r"%ReM0vE%"
        clean_name = re.sub(reg, " ", clean_name)

        # Remove parentheses
        reg = r'\([^)]*\)'
        clean_name = re.sub(reg, " ", clean_name)
        reg = r'\[.*?\]'
        clean_name = re.sub(reg, " ", clean_name)

        # Remove excessive space
        reg = r'\s+'
        clean_name = re.sub(reg, " ", clean_name).strip()

        # Replace space with underscore
        reg = r'\s'
        clean_name = re.sub(reg, "_", clean_name)

        # Remove _+_ and _-_
        reg = r'\_\+\_|\_\-\_'
        clean_name = re.sub(reg, "_", clean_name)

        return clean_name.strip().title()

    @staticmethod
    def remove_year_number(og_string: str) -> str:
        # Remove years
        reg = r'\d{4}'
        potential_years = re.findall(reg, og_string)
        for year in potential_years:
            if int(year) >= 1950 and int(year) <= 2030:
                # print(f"Find year {year}, removing it")
                og_string = re.sub(rf'{year}', " ", og_string)
        return og_string
    
    @staticmethod
    def create_folder_if_not_exists(folder_path: str) -> None:
        if not os.path.exists(folder_path):
            try:
                os.makedirs(folder_path)
                print(f"Folder '{folder_path}' created successfully.")
            except OSError as e:
                print(f"Error creating folder '{folder_path}': {e}")
        else:
            print(f"Folder '{folder_path}' already exists.")

    @staticmethod
    def get_file_extention_name(file_name: str) -> str:
        [name, extension] = os.path.splitext(file_name)
        return extension


class _Season:
    def __init__(self):
        self.episodes = {}

    def __setitem__(self, key, item):
        self.episodes[key] = item

    def __getitem__(self, key):
        return self.episodes[key]

    def __iter__(self):
        return iter(self.episodes.keys())


class _Epsiode:
    def __init__(self, full_path: str):
        self.location = full_path
        self.subtitles = {}

        
class _Subtitle:
    def __init__(self, full_path: str):
        self.location = full_path
        

class SeasonMap:
    def __init__(self, file_system: list):
        """The mapping information that maps file path to season number, it should contain the season number for every file or folder, if not appliable than, NA.

        Args:
            full_path (str): Root dir for the map
        """
        self.fs = file_system
        #print(json.dumps(file_system, indent=2))
        self.root = file_system[0][0]
        self.map = {}

        """Entry point for finding the season number
        """
        basename = os.path.basename(os.path.normpath(self.root))
        # If no better idea later, just use the top one
        if (root_seaon_number := SeasonMap.extract_season_number(basename)) != None:
            self.map = {self.root: root_seaon_number}
        else:
            self.map = {self.root: [1]}

        for root, dirs, files in self.fs:
            for _dir in dirs:
                _season_meta = SeasonMap.extract_season_number(_dir)
                working_dir = os.path.join(root, _dir)
                if _season_meta == None:
                    self.map[working_dir] = self.map[root]
                else:
                    self.map[working_dir] = _season_meta

            
            for _file in files:
                _season_meta = SeasonMap.extract_season_number(_file)
                working_dir = os.path.join(root, _file)
                if _season_meta == None:
                    self.map[working_dir] = self.map[root]
                else:
                    self.map[working_dir] = _season_meta

    def __getitem__(self, full_path: str) -> Union[str, None]:
        try:
            result = self.map[full_path][0]
        except KeyError:
            return None
        return str(result)        

    def all_seasons(self) -> set:
        """Generalize all the seasons that the SeasonMap found

        Returns:
            set: set of seasons
        """
        all_seasons = set()
        for i in self.map.values():
            all_seasons.update([str(j) for j in i])
        return all_seasons


    @staticmethod
    def extract_season_number(dir_name: str) -> list:
        dir_name = Series.clean_name(dir_name)
        dir_name = Series.remove_year_number(dir_name)

        season_number_candidates = set()

        # Reg search for OVA, SP, OAD
        reg = r"\b(OVA|SP|OAD|Special|EXTRA)\b"
        reg = re.compile(reg, flags=re.IGNORECASE)
        season_number_candidates.update([i.lower() for i in re.findall(reg, dir_name)])

        # Reg search for seasons: S01-S12
        reg = r'S(\d{1,2})-S(\d{1,2})'
        reg = re.compile(reg, flags=re.IGNORECASE)
        season_sequence_search = re.findall(reg, dir_name)
        if len(season_sequence_search) == 1:
            lower = season_sequence_search[0][0]
            upper = season_sequence_search[0][1]
            _lu = [lower, upper]
            _lu = [int(i) for i in _lu]
            _lu = sorted(_lu)
            season_number_candidates.update([i for i in range(_lu[0], _lu[1] + 1)])

        # Strict search for formated seasons "- 1x12 - "
        reg = r'\-\s(\d{1})x\d{2}\s\-'
        season_sequence_search = re.findall(reg, dir_name)
        season_number_candidates.update(season_sequence_search)

        # Reg search for "Season"
        reg = r'(?:Season|S)[\s]*?(\d{1,2})'
        reg = re.compile(reg, flags=re.IGNORECASE)
        season_number_candidates.update([int(i) for i in re.findall(reg, dir_name)])
        
        if len(season_number_candidates) > 0:
            return [i for i in season_number_candidates]
        else:
            return None

class EpisodeMap:
    def __init__(self, file_system: list):
        self.fs = file_system
        self.map = {}
        self.reverse_map = {}

        for root, dirs, files in self.fs:
            local_map = EpisodeMap.find_episode_number(files)
            if local_map is None:
                continue
            for _file in local_map:
                full_path = os.path.join(root, _file)
                self.map[full_path] = local_map[_file]

        for key in self.map:
            self.reverse_map[self.map[key]] = key
        #print(json.dumps(self.map, indent=2))
    
    def search(self) -> None:
        return

    def __getitem__(self, full_path: str) -> Union[str, None]:
        try:
            result = self.map[full_path]
        except KeyError:
            return None
        return str(result)   

    def __iter__(self):
        return iter(self.map.keys())

    @staticmethod
    def find_episode_number(files: list) -> dict:
        """Find episode number mapping for 0 depth folders, it only utilize the local context to filter numbers

        Args:
            files (list): The directory to construct the mapping

        Returns:
            dict: The mapping in the format of {file_name(not full path): ep_no}
        """
        if len(files) == 0:
            # Return nothing if no ep is in the folder
            return
        elif len(files) == 1:
            # Turn off context if it is only one
            _testee = files[0]
            numbers = EpisodeMap.extract_ep_numbers(_testee)
            if len(numbers) != 0:
                return {_testee: numbers[0]}
            else:
                return {_testee: 1}
        else:
            # Turn on context
            # Build context
            parent_context = {}
            for _testee in files:
                remove_symbols = EpisodeMap.extract_ep_numbers(_testee)

                local_context = set()
                for word in remove_symbols:
                    word = word.lower()
                    # This is how to calculate Doc Freq
                    if word in local_context:
                        continue # Skip multiple occurance in one name
                    else:
                        local_context.add(word)
                    try:
                        parent_context[word] += 1
                    except KeyError:
                        parent_context[word] = 1

            # Cal the Doc Freq
            for key, value in parent_context.items():
                parent_context[key] = value / len(files)
            #print(parent_context)
            # Find ep number based on reg and context
            result = {}
            for _testee in files:
                numbers = EpisodeMap.extract_ep_numbers(_testee)
                #print(numbers)
                scoring = {}
                for _number in numbers:
                    if _number in parent_context:
                        scoring[_number] = parent_context[_number]
                # Sort the score
                try:
                    scoring = [int(k) for k, v in sorted(scoring.items(), key=lambda item: item[1])]
                    result[_testee] = scoring[0]
                except IndexError:
                    print(f"{_testee} causes ep fail to find number")
                #print(scoring)
        # TODO: Infer from missing number
        return result

    @staticmethod
    def extract_ep_numbers(file_name: str) -> list:
        clean_name = Series.clean_name(file_name)
        [basename, _] = os.path.splitext(clean_name)
        reg = r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?\\|`~=-]'
        remove_symbols = re.sub(reg, " ", basename) # TODO: May use a more clever split in the future
        reg = r'[A-Za-z]'
        remove_symbols = re.sub(reg, " ", remove_symbols).strip()
        # Remove years
        remove_symbols = Series.remove_year_number(remove_symbols)
        
        reg = r'\d{1,2}'
        numbers = re.findall(reg, remove_symbols)
        #print(numbers)
        return numbers