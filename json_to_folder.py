import os
import json

def create_folder_structure(data, base_path):
    for item in data['contents']:
        item_type = item['type']
        item_name = item['name']
        item_path = os.path.join(base_path, item_name)

        if item_type == 'folder':
            os.makedirs(item_path, exist_ok=True)
            create_folder_structure(item, item_path)
        elif item_type == 'file':
            with open(item_path, 'w') as file:
                pass  # Create an empty file

def main():
    json_file = input("Enter the path of the JSON file: ")

    if not os.path.exists(json_file):
        print("JSON file does not exist.")
        return

    with open(json_file, 'r') as file:
        json_data = json.load(file)

    target_directory = input("Enter the target directory where you want to recreate the structure: ")

    if not os.path.exists(target_directory):
        print("Target directory does not exist.")
        return

    create_folder_structure(json_data, target_directory)
    print("Folder structure has been recreated.")

if __name__ == "__main__":
    main()