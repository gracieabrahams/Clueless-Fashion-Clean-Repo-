"""my idea here:
make csv into a python dictionary
use the python dictionary in the js file"""

'''import csv

# Replace 'path/to/your/file.csv' with the actual path to your CSV file
csv_file_path = '/Users/Grace/Downloads/clean_clothing.csv'

# Create an empty dictionary to store the clothing data
clothing_database = {}

# Read the CSV file and organize the data into the dictionary
with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    for row in csv_reader:
        type_ = row['type']
        url = row['url']
        name = row['name']

        if type_ not in clothing_database:
            clothing_database[type_] = []

        # Generate a unique ID within each type
        item_id = len(clothing_database[type_]) + 1

        clothing_database[type_].append({'id': item_id, 'name': name, 'image': url})

# Display the resulting clothing_database
print(clothing_database)'''

import csv
# Replace 'path/to/your/output/file.txt' with the desired path for the output text file
output_txt_path = '/Users/Grace/Downloads/clean_clothing_output.txt'

# Your existing code to read the CSV file and organize the data into the dictionary
csv_file_path = '/Users/Grace/Downloads/clean_clothing.csv'
clothing_database = {}

with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for row in csv_reader:
        type_ = row['type']
        url = row['url']
        name = row['name']

        if type_ not in clothing_database:
            clothing_database[type_] = []

        item_id = len(clothing_database[type_]) + 1

        clothing_database[type_].append({'id': item_id, 'name': name, 'image': url})

# Writing the output to a new text file
with open(output_txt_path, 'w') as txtfile:
    for type_, items in clothing_database.items():
        txtfile.write(f"{type_}:\n")
        for item in items:
            txtfile.write(f"  {item}\n")

