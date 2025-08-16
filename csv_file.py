import csv

file_name = "domain_info.csv"

with open(file_name, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
