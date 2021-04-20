import json
import csv
import os


# Opening JSON file and loading the data
# into the variable data
with open('data.json') as json_file:
    data = json.load(json_file)

full_data = data['details']

# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing 
# headers to the CSV file
count = 0

for i in full_data:
    if count == 0:

        # Writing headers of CSV file
        header = i.keys()
        csv_writer.writerow(header)
        count += 1
        
    # Writing data of CSV file
    csv_writer.writerow(i.values())
data_file.close()

