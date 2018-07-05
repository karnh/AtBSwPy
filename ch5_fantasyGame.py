def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory

def displayInventory(inv):
    # code
    total = 0
    print('Inventory:')
    for k, v in inv.items():
        print(str(v).rjust(3) + ' ' + k)
        total += v

    print('\nTotal number of items:', total)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)