import csv

with open('countries.csv') as myFile:  
    reader = csv.DictReader(myFile)
    for row in reader:
        print(row['capital'])