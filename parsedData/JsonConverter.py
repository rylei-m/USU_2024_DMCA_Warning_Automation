import json
import os
from XMLforDMCA.Config import JSON_DIR, JSON_BASE_NAME, JSON_EXTENSION
from XMLforDMCA.parsedData.JsonUtils import normalize_keys, key_mappings

json_file_path = os.path.join(JSON_DIR, f"{JSON_BASE_NAME}{JSON_EXTENSION}")


def load_json_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {JSON_DIR} does not exist.")

    with open(file_path, 'r') as file:
        j_data = json.load(file)
    return j_data


try:
    json_data = load_json_data(json_file_path)
    json_data = normalize_keys(json_data, key_mappings)
except FileNotFoundError as e:
    print(e)
    json_data = {
        "Data": {
            "Contact": "",
            "Title": "",
            "IP_Address": "",
            "Type": "",
            "Filename": "",
            "Timestamp": "",
            "SubType.Protocol": "",
            "Entity": ""
        }
    }


data = json_data['Data']
Username = data['Contact']
Title = data['Title']
Contact = data['Contact']
IP_Address = data['IP_Address']
Type = data['Type']
Filename = data['Filename']
Timestamp = data['Timestamp']
SubType_Protocol = data['SubType.Protocol']
Entity = data['Entity']
