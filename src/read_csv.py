import sys
import csv
filename = sys.argv[1]
fields = []
rows = []
with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
    #csvwriter = csv.writer(csvfile)
	# extracting field names through first row
	fields = next(csvreader)
	#print(fields)
	for row in csvreader:
		rows.append(row) 
	#print("Total no. of rows: %d"%(csvreader.line_num))
print('Field names are:' + ', '.join(fields))
for row in rows[1:]:
	# parsing each column of a row
	for col in row:
		print("%10s"%col,end=" "),
	print('\n')


