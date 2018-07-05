#! python3
# backupToZip.py - copies entire folder and its contents into
# a zip file whose filename increments

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of a "folder" into a zip file.
    folder = os.path.abspath(folder)

    # Get zip filename
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1

    # Create zip file
    print('creating {} ...'.format(zipFileName))
    backupZipFile = zipfile.ZipFile(zipFileName, 'w')

    # Walk entire tree and compress into folder
    for fname, subfolders, files in os.walk(folder):
        print('Adding files in {} ...'.format(fname))
        # Add current folder to zip
        backupZipFile.write(fname)
        # Add all files in this folder to zip
        for file in files:
            newBase = os.path.basename(folder) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue
            backupZipFile.write(os.path.join(fname, file))

    backupZipFile.close()
    print('Done')

backupToZip('C:\\Users\\hkarn\\Downloads\\example')