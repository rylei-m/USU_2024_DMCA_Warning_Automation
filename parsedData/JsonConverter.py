import json


def load_json_data(json_file_path):
    with open(json_file_path, 'r') as file:
        j_data = json.load(file)
    return j_data


json_data = load_json_data('/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/parsedData/parsedData.json')

data = json_data['Data']
Username = data['Contact']
Title = data['Title']
Contact = data['Contact']
Type = data['Type']
FileName = data['FileName']
Timestamp = data['TimeStamp']
SubType_Protocol = data['SubType.Protocol']
