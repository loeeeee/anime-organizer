from series import Series, SeriesShouldBeDir
import os
from typing import Literal, Union

working_dir = "test/mimic/" # Source media
target = "test/target/" # Target directory where the symbolic link 

def main() -> None:
    base_dir = os.getcwd()
    Series.create_folder_if_not_exists(target)

    series_list = set()
    for series_base_dir in os.listdir(working_dir):
        try:
            _series = Series(os.path.join(base_dir, working_dir, series_base_dir))
        except SeriesShouldBeDir:
            continue
        _series.display()
        if str(_series) not in series_list:
            series_list.add(str(_series))
        else:
            print(f"{str(_series)} already exists")
            continue

        _series.link(target)
        print()

if __name__ == "__main__":
    main()