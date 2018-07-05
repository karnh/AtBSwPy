tableData = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'Davidmos'], 
             ['dogs', 'cats', 'moose', 'goose']]

def tablePrint(table):
    colLengths = []
    for row in table:
        for i in range(len(row)):
            try:
                maxLen = colLengths[i]
            except IndexError:
                colLengths.append(0)
                maxLen = 0
            if len(row[i]) > maxLen:
                colLengths[i] = len(row[i])

    for row in table:
        for i in range(len(row)):
            print(row[i].rjust(colLengths[i]+1), end='')
        print()


    print(colLengths)

tablePrint(tableData)