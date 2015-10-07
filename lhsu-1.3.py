#!/usr/bin/env python

#introduce game and the rules
print ('*Number Guessor*')
print ('Think of an integer between 100 and 0, and I will try to guess it.')

#defines initial variables for guess and number boundaries
guess = 50
upper_bound = 100
lower_bound = 0
end = 0 #variable to break the while loop once we have won

#defining absolute boundaries for the guesses
maxval = 99
minval = 1

#defining strings to use for comparison against user input later
no = "no"
yes = "yes"
lower = "lower"
higher = "higher"
quit = "quit"

while end == 0 :
    yesno = input('Is it ' + str(guess) + '? (say yes/no/quit) ')
    print yesno
    guess_up = guess + 1 #variable for comparing against boundaries
    guess_down = guess - 1 #variable for comparing against boundaries
    if yesno is no:
        highlow = input('Is it higher or lower than ' + str(guess) + '? ')
        if highlow is higher:
            if guess == maxval:
                print ('You either changed your number or picked a number too large for me to handle... womp')
                end = 1
                break
            elif guess_up == upper_bound: 
                print guess_up
                print upper_bound
                print ('You changed your number... womp')
                break
            else:
                lower_bound = guess
        elif highlow is lower:
            if guess == minval:
                print ('You either changed your number or picked a number too small for me to handle... womp')
                end = 1
                break
            elif guess_down == lower_bound:
                print ('You changed your number... womp')
            else:
                upper_bound = guess
        else:
            print ('Try again. Either say higher or lower')
            highlow = input('Is it higher or lower than ' + str(guess) + '?')
        guess = ((upper_bound - lower_bound)/2) + lower_bound
        if guess > maxval:
            print ('You either changed your number or picked a number too large for me to handle... womp')
            end = 1
        elif guess < minval:
            print ('You either changed your number or picked a number too small for me to handle... womp')
            end = 1
    elif yesno is yes:
        end = 1
        print ('I knew it!!!')
    elif yesno is quit:
        print ('Bye bye')
        break
    else:
        print ('Your input was not valid. Start over and try me again.')
