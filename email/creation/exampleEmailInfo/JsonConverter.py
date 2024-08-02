import json

json_file_path = "/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/email/creation/exampleEmailInfo/emailInfo.json"


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
            "Group": "",
            "Organization": "",
            "ContactInfo": "",
            "EmailAddress": "",
        }
    }


data = json_data['Data']
Group = data['Group']
Organization = data['Organization']
ContactInfo = data['ContactInfo']
EmailAddress = data['EmailAddress']
