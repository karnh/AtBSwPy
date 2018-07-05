#! python3
# Zip folder content to a zip file with a incrementing number suffix

import os, sys, zipfile, re

if len(sys.argv) > 1:
    path = sys.argv[1]

    if (os.path.exists(path) and os.path.isdir(path)):
        # Find archive sequence number
        archivePattern = re.compile( '^' + os.path.basename(path) + '_' + '(.*).zip$')
        archiveCount = 1
        for file in os.listdir(os.path.dirname(os.path.abspath(path))):
            mo = archivePattern.search(file)
            if mo is not None:
                archiveCount += 1
        
        # Zip file contents
        zipFile = zipfile.ZipFile(os.path.abspath(path) + '_' + str(archiveCount) + '.zip', 'w')

        for file in os.listdir(path):
            zipFile.write(os.path.join(path,file), compress_type=zipfile.ZIP_DEFLATED)

        zipFile.close()
    else:
        print('Invalid directory \'{}\'. Please provide a valid direcotry.'.format(sys.argv[1]))
else:
    print('Usage: {} [directory_path]'.format(os.path.basename(sys.argv[0])))