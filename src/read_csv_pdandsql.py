from pandasql import sqldf
import pandas as pd
import sys,csv
filename = sys.argv[1]
fields = []
rows = []
with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)
	for row in csvreader:
		rows.append(row) 

pysqldf = lambda q: sqldf(q, globals())
query = f"SELECT * FROM {rows} LIMIT 3"
print(pysqldf(query))
