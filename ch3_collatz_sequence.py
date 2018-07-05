def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

#print('Enter a number: ', end = '')
try:
    input = int(input('Enter a number: '))
except:
    print('Not a number')

num = input
count = 0
while num != 1 and count < 100000:
    num = collatz(num)
    print(num)
    count += 1