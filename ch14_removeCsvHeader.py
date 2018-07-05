#! python3
# removeCsvHeader.py - Remove the header from all csv files

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop over all csv files
for filename in os.listdir('removeCsvHeader'):
    if filename.endswith('.csv'):
        print('Removing header from {} ...'.format(filename))

        # Read csv file
        csvRows = []
        csvFileObj = open(os.path.join('removeCsvHeader', filename))
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num != 1:
                csvRows.append(row)
        csvFileObj.close()

        # write csv file
        csvFileObj = open(os.path.join('headerRemoved', filename), 'w', newline='')
        csvWriter = csv.writer(csvFileObj)
        for row in csvRows:
            csvWriter.writerow(row)
        csvFileObj.close()