birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar14'}

while True:
    name = input('Enter a name (Blank to quit): ')
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I don\'t have birthday of ' + name)
        bday = input('What\'s your birthday?')
        birthdays[name] = bday
        print('DB Updated')