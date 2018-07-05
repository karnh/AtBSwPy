import os

for foldName, subFolds, files in os.walk('c:\\Dell'):
    print('current folder is {}'.format(foldName))

    for subFolder in subFolds:
        print('SUBFOLDER OF {}: {}'.format(foldName, subFolder))

    for fileName in files:
        print('FILE INSIDE {}: {}'.format(foldName, fileName))