import os,re,sys

reg = re.compile(sys.argv[1])

for file in os.listdir('.'):
    if os.path.isfile(file):
        fileHandle = open(file)
        for line in fileHandle.readlines():
            if reg.search(line) is not None:
                print ('{}: {}'.format(file, line.replace('\n','')))