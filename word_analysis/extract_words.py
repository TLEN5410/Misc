import csv

with open('quiz2_muddiest.csv') as f:
     csvreader = csv.reader(f)
     data = [r[14] for r in csvreader]
