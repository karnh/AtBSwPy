while True:
    age = input('Your age? ')
    if age.isdecimal():
        break
    print('Age can only be numbers')

while True:
    passwd = input('Your password? ')
    if passwd.isalnum():
        break
    print('Only alnum passwd')