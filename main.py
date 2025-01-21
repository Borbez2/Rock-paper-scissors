import random

choices = ['rock', 'paper', 'scissors']

# Loop to make sure they enter a valid choice
while True:
    computer = random.choice(choices)
    player = input('rock, paper, or scissors? ').lower()

    if player not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    print('Computer:', computer)
    print('Player:', player)

    # Determine the winner :>
    if player == computer:
        print('DRAW!')
    elif player == 'rock':
        if computer == 'paper':
            print('Computer wins!')
        else:
            print('Player wins!')
    elif player == 'paper':
        if computer == 'scissors':
            print('Computer wins!')
        else:
            print('Player wins!')
    elif player == 'scissors':
        if computer == 'rock':
            print('Computer wins!')
        else:
            print('Player wins!')

    # Play again???
    play_again = input('Play again? (yes/no): ').lower()
    if play_again != 'yes':
        print('Thanks for playing!')
        break
