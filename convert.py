# this is used to extract necessary fields from data file. Here school_name, Latitude, Longitude, Selective_school fields are extracted for generating map.
# Collections.csv file is the original dataset used for study purpose
import csv
users_dict = {}
with open('out.csv', 'w') as f: # output csv file
    writer = csv.writer(f)
    writer.writerow(['School_name', 'Latitude', 'Longitude', 'Selective_school'])
    with open('collections.csv','r') as csvfile: # input csv file
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            writer.writerow([row['School_name'], row['Latitude'],row['Longitude'], row['Selective_school']])
            users_dict.update(row)
