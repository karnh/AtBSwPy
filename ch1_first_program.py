print('Hello World')
print('What is your name?')
#myName = input()
#print('Nice to meet you' + myName +  ' :length: ', str(len(myName)))

name = 'a'

while name != 'a':
    print('not a')
    name = input()

print('Thank you')

def spam():
    print(eggs)
    #eggs = 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)