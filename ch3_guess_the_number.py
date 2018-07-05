import random

secretNumber = random.randint(1,20)
print('I\'ve a number between 1 and 20')

# Guess 6 times
for guessTaken in range(1,7):
    print('Take a guess')
    try:
        guess = int(input())
    except:
        print('NaN')
        continue

    if guess > secretNumber:
        print('Too high.')
    elif guess < secretNumber:
        print('Too low')
    else:
        print('You guessed my num ' + str(guessTaken) + ' guesses')
        break

if guess != secretNumber:
    print('Nope. The number I was thinking is ' + str(secretNumber))