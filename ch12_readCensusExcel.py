#! python3
# readCensusExcel.py - Tabulates population and number of census tracts
# for each county.

import openpyxl, pprint
print('Opening workbook ...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# Fill countyData with each county population and tracts
print('Reading rows ...')

for row in range(2, sheet.max_row + 1):
    # Each row has census data for 1 tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for state exists
    countyData.setdefault(state, {})
    # Make sure key for this county in this state exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row is one tract
    countyData[state][county]['tracts'] += 1
    # Update population
    countyData[state][county]['pop'] += int(pop)

# Write countyData to file
print('Writing results ...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')