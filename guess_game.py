# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# intialize globals
secret_number = 0
num_range = 100
no_of_attempts = int(math.ceil(math.log(num_range, 2)))

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global no_of_attempts
    #secret_number = random.randrange(0, num_range)
    secret_number = 43
    no_of_attempts = int(math.ceil(math.log(num_range, 2)))
    print 'New Game. Range is from 0 to', num_range
    print 'Number of remaining guesses is', no_of_attempts
    print

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()    
  
def input_guess(guess):
    # main game logic goes here	
    global no_of_attempts
    
    no_of_attempts -= 1
    
    if (no_of_attempts >= 0):
        print 'Guess was', guess
        print 'Number of remaining guesses is', no_of_attempts
        user_guess = int(guess)         
        if (user_guess > secret_number): 
            result = 'Lower'
        elif (user_guess < secret_number):
            result = 'Higher'   
        else:
            result = 'Correct'
    else:        
        result = 'You ran out of guesses. The number was ' + str(secret_number)
    

    print result    
    print
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.add_input("Enter", input_guess, 200)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
