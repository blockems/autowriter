import os
import json

def process_file(file_path):
    with open(file_path, "r") as file:
        content = file.read().splitlines()
    return content

def save_to_json(data, output_filename):
    with open(output_filename, "w") as json_file:
        json.dump(data, json_file)

articles_directory = "articles"
subjects_directory = "subjects"

if not os.path.exists(subjects_directory):
    os.makedirs(subjects_directory)

print(f"Processing files in {articles_directory}...")

for file in os.listdir(articles_directory):
    file_path = os.path.join(articles_directory, file)
    
    if os.path.isfile(file_path):
        print(f"Processing {file_path}...")
        # Process the file and turn it into a JSON list
        json_data = process_file(file_path)

        # Save the JSON list to the subjects directory
        output_filename = os.path.join(subjects_directory, file.replace(".txt", ".json"))
        save_to_json(json_data, output_filename)
        print(f"Processed and saved {file_path} as {output_filename}")
    else:
        print(f"Skipping {file_path} (not a file)")

print("Processing complete.")
