import xml.etree.ElementTree as ET
import json
import os
from XMLforDMCA.incoming.parser import extract_data, strip_namespace


def main(path):
    tree = ET.parse(path)
    root = tree.getroot()
    data = extract_data(root)
    return {
        "Root element": strip_namespace(root.tag),
        "Data": data
    }


def get_unique_filename(directory, base_name, extension):
    i=1
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


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_path = '/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/testFiles/demoIgnore.xml'

    output_dir = '/home/ryleim/PycharmProjects/XMLforDMCA/XMLforDMCA/parsedData/JSONS'
    base_name = "parsedData"
    extension = ".json"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_data = main(xml_path)
    output_path = save_to_json(output_data, output_dir, base_name, extension)

    print(f"Data saved to {output_path}")
