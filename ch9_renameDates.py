#! python3
# Renames files with american format data in its name to european format
# American format - mm-dd-yyyy, European format - dd-mm-yyyy
import os, re, shutil

dateRegex = re.compile(r'(.*)(\d{2})-(\d{2})-(\d{4})(.*)')

# List all directory
for file in os.listdir('.'):
    # Regex match
    matchResult = dateRegex.search(file)
    if matchResult is not None:
        newFile = matchResult[1] + matchResult[3] + '-' + matchResult[2] + '-' + matchResult[4] + matchResult[5]
        shutil.move(file, newFile)