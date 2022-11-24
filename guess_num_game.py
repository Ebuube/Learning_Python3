#!/usr/bin/env python

# Guess a number :game

import random
import math    # for log2()

# the number of trials for th user
line = ('=' * 60) + '\n'

# Introduce the game to the user
def intro():
	print(line)
	print('Try and guess the number the computer is thinking.:)')
	print(line)
# end of function

# Get the appropriate input from the user
def fetch_input(val_int):
	while True:
		val_int = input('What number is the computer thinking? ')
		isint = True
		try:
			val_int = int(val_int)
		except:
			print('Error:	Enter an integer\n')
			isint = False
			
		if isint == True:
			return val_int	
# end of function

# Declare the result of the game
def result(usr, cmpt):
    if usr == cmpt:
        print('What a successful guess!'
            '\nYou win!')
    else:
        print('You lose')
        print('Sorry, the computer thought of ' + str(cmpt))
# end of function

# Message before exitting
def closure():
	print('\n' + line)
	print('Brainspark Games By:\n'
	'\tOnwuta Ebube Gideon')
	print(line)
# end of function

# Function to set Level
def set_level():
    level = int()

    # get level
    while True:
        isint = True
        level = input('Enter level (1/2/3/etc): ')
        try:
            level = int(level)
        except:
            isint = False

        if isint == False:
            print('Sorry, enter an integer\n')
            continue
        else:
            break
        # end of while

    return level
# end of function


# Function to Declare Game Level and Trials
def declare_L_and_T(L, T):
    print('\nYou are playing Level ' + str(L))
    print('The computer is thinking of a number between 0 and ' + str(L * 10))
    print('You have ' + str(T) + ' trial(s)')
    print('Goodluck')
    print(line)
# end of function


# Function to Play the game
def play():
    level = set_level()
    u_bound_guess = level * 10
    cmpt_guess = random.randint(0, u_bound_guess)
    trials = math.log(u_bound_guess, 2)
    trials = int(trials) + 1
    usr_guess = 0

    declare_L_and_T(level, trials)
	
    for count in range(trials):
        usr_guess = fetch_input(usr_guess)
        if usr_guess == cmpt_guess:
            break
        elif usr_guess < cmpt_guess:
            print('Your guess is too low\n')
        elif usr_guess > cmpt_guess:
            print('Your guess is too high\n')

    result(usr_guess, cmpt_guess)
# end of function


# Program starts officially

intro()

play()

closure()
