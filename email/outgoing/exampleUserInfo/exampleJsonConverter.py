import json

json_file_path = "YOUR_FILE_PATH_HERE"


def load_json_data(file_path):
    with open(file_path, 'r') as file:
        j_data = json.load(file)
    return j_data


try:
    json_data = load_json_data(json_file_path)
except FileNotFoundError as e:
    print(e)
    json_data = {
        "Data": {
            "UserEmail": "",
            "Password": "",
            "EmailTo": ""
        }
    }


data = json_data['Data']
UserEmail = data['UserEmail']
Password = data['Password']
EmailTo = data['EmailTo']
