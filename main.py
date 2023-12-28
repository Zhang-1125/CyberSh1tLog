import csv

FileName = 'DataSheet.csv'
with open(FileName) as DataSheet:
    reader = csv.reader(DataSheet)
for row in reader:
    print(row)
