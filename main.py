import time
import sys
import random

affirmative_answers = ["yes", "yeah", "sure", "yup", "okay", "of course", "alright", "certainly", "absolutely", "by all means", "yup", "ok", "okie", "yea", "why not", "lets begin"]
negative_answers = ["naw", "never", "absolutly not""no", "nope", "nah","not a chance", "sorry", "never", "no way"] 

def win():
    print('\nYou win!')

def lost():
    print('\nYou lost.')

def draw():
    print('\nIts a draw!')

ans = input("\nHi, welcome to Rock, Paper, Scissors. Do you want to play? ")
if ans in affirmative_answers:
  print("\nLets Play!")

else:
  ans = input("\nAre you sure? ")

  if ans in affirmative_answers:
    print("\nI knew you would change your mind! Lets play!")
  else:
    print("\nGood Bye")


def the_game():

    moves = ['rock', 'paper', 'scissors']

    print(' \nRock, Paper, Scissors?')
    attempts = 3
    while True:
        if attempts == 0:
            print('\nYou failed to provide a correct option to play the game.')
            time.sleep(3)
            sys.exit(0)

        player = str(input('Player: ')).lower()
        if player.lower() not in moves:
            print(f' \nYou entered an invalid option! You have {attempts} attempts left.')
            attempts -= 1
        else:
            computer = random.choice(moves)
            print(f'\nComputer: {computer}')

            if player == computer:
                draw()
            elif player == 'rock' and computer == 'scissors':
                win()
            elif player == 'rock' and computer == 'paper':
                lost()
            elif player == 'paper' and computer == 'rock':
                win()
            elif player == 'paper' and computer == 'scissors':
                lost()
            elif player == 'scissors' and computer == 'paper':
                win()
            elif player == 'scissors' and computer == 'rock':
                lost()
            else:
                pass

            play_again = str(input('\nDo you want to play again? (y/n): '))
            if play_again.lower() == 'y':
                the_game()
            elif play_again.lower() == 'n':
                print('\nGoodbye.')
                time.sleep(2.5)
                sys.exit(0)
            else:
                print('\nYou entered an invalid option. Goodbye.')
                time.sleep(2.5)
                sys.exit(0)


if __name__=='__main__':
    the_game()