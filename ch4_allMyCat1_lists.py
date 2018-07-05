catNames = []

while True:
    name = input('Enter the name of cat ' + str(len(catNames) + 1) + ' (enter to stop): ')
    if name == '':
        break

    catNames = catNames + [name]

print('Cat names are : ' )
for name in catNames:
    print('  ' + name)

def eggs(val):
    val.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)

def listItems(list):
    item_list = ''
    for index in range(0,len(list) - 1):
        item_list += str(list[index]) + ', '

    item_list = item_list[:-2] + ' and ' + list[-1]
    print(item_list)

fruits = ['appl', 'babanan', 'orage']
names = ['harsh']
empty = []
listItems(fruits)
listItems(spam)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

grid_len = len(grid)
grid_item_len = len(grid[0])

for x in range(grid_item_len):
    for y in range(grid_len):
        print(grid[y][x], end='')
    print('')

