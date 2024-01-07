import os
import json

def folder_to_json(folder_path):
    data = {
        'name': os.path.basename(folder_path),
        'type': 'folder',
        'contents': []
    }

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            data['contents'].append(folder_to_json(item_path))
        else:
            data['contents'].append({
                'name': item,
                'type': 'file'
            })

    return data

def main():
    folder_path = input("Enter the path of the folder to convert to JSON: ")

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    json_data = folder_to_json(folder_path)

    with open('folder_structure.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print("Folder structure has been saved to 'folder_structure.json'")

if __name__ == "__main__":
    main()