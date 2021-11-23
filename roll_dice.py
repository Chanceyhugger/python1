import random
roll = random.randint(1,6)
guess = int(input('guess the dice roll:\n'))
if roll == guess:
    print('you are very smart my friend, ' + str(guess) + ' was correct')
else:
    print('ew ' + str(guess) + " is not the right answer. it was " + str(roll))