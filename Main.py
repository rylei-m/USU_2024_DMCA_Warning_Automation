import xml.etree.ElementTree as ET
import os

from XMLforDMCA.Config import JSON_DIR, XML_PATH, JSON_BASE_NAME, JSON_EXTENSION
from XMLforDMCA.email.creation.EmailTemplate import generated_email_subject, generated_email_body
from XMLforDMCA.email.outgoing.EmailGenerator import sender
from XMLforDMCA.parsedData.JsonUtils import save_to_json
from XMLforDMCA.incoming.parser import extract_data, strip_namespace


def main(path):
    tree = ET.parse(path)
    root = tree.getroot()
    data = extract_data(root)
    return {
        "Root element": strip_namespace(root.tag),
        "Data": data
    }


if __name__ == '__main__':
    if not os.path.exists(JSON_DIR):
        os.makedirs(JSON_DIR)

    output_data = main(XML_PATH)
    output_path = save_to_json(output_data, JSON_DIR, JSON_BASE_NAME, JSON_EXTENSION)

    print(f"Data saved to {output_path}")

    generated_email_subject()
    generated_email_body()
    sender()
