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


def load_json_data(file_path):
    """Load JSON data from a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        return json.load(file)


def normalize_keys(data, key_mappings):
    """Normalize dictionary keys according to the provided key_mappings."""
    normalized_data = {}
    for key, value in data.items():
        # Check if current key should be normalized
        normalized_key = key_mappings.get(key, key)
        if isinstance(value, dict):
            # Recursively normalize keys in nested dictionaries
            normalized_data[normalized_key] = normalize_keys(value, key_mappings)
        else:
            normalized_data[normalized_key] = value
    return normalized_data


key_mappings = {
    "FileName": "Filename",
    "TimeStamp": "Timestamp"
}
