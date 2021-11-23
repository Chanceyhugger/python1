import random


computer_choice = random.choice(['paper', 'scissors', 'rock'])

user_choice = input('do you want - rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print('tie')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('you win')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('you win')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('you win')
else:
    print('you lose haha loser it was actually ' + computer_choice)