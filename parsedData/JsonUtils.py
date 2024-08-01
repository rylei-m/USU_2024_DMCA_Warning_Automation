import os
import json


def get_unique_filename(directory, base_name, extension):
    i = 1
    while True:
        filename = f"{base_name}{'' if i ==1 else i}{extension}"
        if not os.path.exists(os.path.join(directory, filename)):
            return filename
        i += 1


def save_to_json(data, directory, base_name, extension):
    filename = get_unique_filename(directory, base_name, extension)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    return file_path
