import random
i = random.randint(1, 9)

c = 1
for j in range(1, 10):
    gn = int(input('Guess the number between 1 to 9'))
    if i == gn:
        print('Perfectly Guessed!! as',gn, 'and guess number of times is',c)
        break
    else:
        print('Sorry!! You guessed the wrong one\n')
        print('Again',end=' ')
        c += 1
