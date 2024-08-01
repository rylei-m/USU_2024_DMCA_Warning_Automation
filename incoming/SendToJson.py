import os

from XMLforDMCA.Config import XML_PATH, JSON_DIR, JSON_BASE_NAME, JSON_EXTENSION
from XMLforDMCA.Main import main
from XMLforDMCA.parsedData.JsonUtils import save_to_json

if not os.path.exists(JSON_DIR):
    os.makedirs(JSON_DIR)

output_data = main(XML_PATH)
output_path = save_to_json(output_data, JSON_DIR, JSON_BASE_NAME, JSON_EXTENSION)  # Save to JSON

print(f"Data saved to {output_path}")
