import names as nm
import time

# Define the weapons
rock = 'rock'
paper = 'paper'
scissors = 'scissors'

# Since this is the backend, I need to define some functions for the main game.
def user_choice():
    userChoice = input('Enter your desired weapon: ')
    if userChoice == rock or userChoice == rock.upper() or userChoice == rock.capitalize():
        print('You chose rock')
        print('Waiting for the computer choice...')
        time.sleep(2)

    elif userChoice == paper or userChoice == paper.capitalize():
        print('You chose paper')
        print('Waiting for the computer choice...')
        time.sleep(2)

    elif userChoice == scissors or userChoice == scissors.capitalize():
        print('You chose scissors')
        print('Waiting for computer choice...')
        time.sleep(2)

    else:
        print('Invalid Command')

def comp_choice():
    pass
