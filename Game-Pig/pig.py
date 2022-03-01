from random import randint

################################################################################################
# Print instruction #
################################################################################################

def print_instructions():
    '''Prints the rules of the game'''
     
    instruction = "----------Instruction----------\nYou have 2 players and each player has a chance to roll a die. If a player rolls any numbers except for 6, those numbers are added to your final score. If a player rolls a 6, then the total score for that turn is 0. The first player to reach or exceed 50 is a winner. If the first player reaches 50 first, then the second player gets one additional turn. On the other hand, if the second player reaches 50, then the first player does not get one additional turn. For a tie, each player gets one additional turn until the tie is broken."

    print(instruction)

###############################################################################################
# Computer move's first  #
###############################################################################################

def computer_move(computer_score, human_score):
    '''Has Computer roll some number of times, displays the result of each roll, and
    returns the result (either 0 or the total value of the rolls).
    Uses the given arguments to play more intelligently.
    '''
    computer_round_score = 0 #this is to keep track of all the numbers rolled in each round 
      
    computer_roll = roll()   #randomly rolls a die
    
    if computer_roll != 6:

        while computer_roll != 6:
            print("Computer rolled {}".format(computer_roll))

            computer_round_score += computer_roll #adds whatever you rolled (except for 6) to your round score computer_round_score 
            computer_score += computer_roll #finds the total computer_score after each round. 

            print("Total computer score: {}".format(computer_score))
            
            if computer_score <= human_score: #playing intelligently by allowing computer to roll one additional time if computer's score is less than human 
                another_roll = roll() 
                #print("Computer rolled {}".format(another_roll))

            
            else:
                return computer_round_score #going back to the normal 

        #if yuo roll a 6: computer_score - computer_round_score 
        computer_rolled_six = computer_score - computer_round_score
        print("Computer score: {}".format(computer_rolled_six))

    else:
        #Think this section as: if computer_roll == 6: 
        computer_rolled_six = computer_score - computer_round_score #need to subtract all of the scores you got in one round if you get a 6 from your total computer_score 
        print("Computer has {} points".format(computer_rolled_six))
        return 0 





###############################################################################################
# Human Move's second #
###############################################################################################

def human_move(computer_score, human_score):
    '''Repeatedly asks whether the user wants to roll again and displays the result of each roll.
    - If the user chooses to roll again, and DOES NOT roll a 6, this function adds the roll
    to the total of the rolls made during this move.
    - If the user chooses to roll again, and DOES roll a 6, the function returns 0.
    - If the user chooses not to roll again, the function returns the total of the rolls made during this move.
    '''
    roll_again = ask_yes_or_no("Do you want to play?(y/n)")

    human_roll = roll() 
    human_round_scores = 0
    count_rolls = 1
    
    # Initial call
     ##Problem is here not asking if human wants to roll 
    print('You rolled {}'.format(human_roll))
    # If not 6 we ask user to play
    if human_roll != 6:
        human_round_scores += human_roll
        roll_again = ask_yes_or_no('Do you want to play? \n') ##chnaged 

        # If true, continue playing
        while roll_again:
            # Roll again
            human_roll = roll() 
            print('You rolled {}'.format(human_roll))

            if human_roll != 6:
                # Add gained points to current turn score
                human_round_scores += human_roll
            else:
                # Reset gained points to 0 if you rolled a 6
                human_round_scores = 0
                return human_round_scores

            count_rolls += 1 
            print ('Your current score is {}'.format(human_round_scores))
            roll_again = ask_yes_or_no('Do you want to play? \n')

            if roll_again == False:
                print("Total times you rolled: {}".format(count_rolls))
            return human_round_scores
    else:
        human_round_scores = 0
    return human_round_scores
    
###############################################################################################
#Checking if the game is over based on scores #
###############################################################################################

def is_game_over(computer_score, human_score):
    '''Returns True if either player has 50 or more, and the players are not tied,
    otherwise it returns False.
    '''
    if (computer_score >= 50 or human_score >= 50) and (computer_score != human_score): #checking if neither one has reached 50 or more and when it's not tie 
        return True

    else:
        return False

###############################################################################################
#Randomly roll a number#
###############################################################################################

def roll():
    '''Returns a random number in the range 1 to 6, inclusive.'''

    rolling_random_number = randint(1,6)

    return rolling_random_number

###############################################################################################
# Asking the prompt again#
###############################################################################################

def ask_yes_or_no(prompt):
    '''Prints the given prompt as a question to the user, for example, 'Roll again? (y/n) '.
    - If the user responds with a string whose first character is 'y' or 'Y', returns True.
    - If the user responds with a string whose first character is 'n' or 'N', returns False.
    - Any other response causes the question to be repeated until the user provides an acceptable response.
    '''
    asking_roll_again = input(prompt) #whatever prompt you add here, it will return your question 
    if asking_roll_again.lower() == 'y':
        return True

    elif asking_roll_again.lower() == 'n':
        return False

    else:
        ask_yes_or_no(prompt) #question repeat 


###############################################################################################
# Displaying the current scores. call this function before and after human_move() #
###############################################################################################

def show_current_status(computer_score, human_score):
    '''Tells the user both her current score and Computer's score, and how far
    behind (or ahead) she is, or if there is a tie.
    ''' 
    #If computer has higher score than human 
    if computer_score > human_score:
        computer_score_difference = computer_score - human_score
        print("\nComputer's score: {}\nYour score: {}\nComputer is ahead by {}.".format(computer_score, human_score, computer_score_difference ))

    elif computer_score < human_score:
        print("\nYour score: {}\nComputer's score: {}. Computer is behind by {}.".format(human_score, computer_score, human_score - computer_score))

    elif computer_score >0 and human_score > 0 and computer_score == human_score:
        print("It is a tie")

###############################################################################################
# At the end of the game, call this function at the end #
###############################################################################################

def show_final_results(computer_score, human_score):
    '''Tells the user whether she won or lost, and by how much.
    '''

    #computer won 
    if computer_score >= 50 and human_score < 50:
        comp_score_difference = computer_score - human_score
        print("You lost. Computer won by {}".format(comp_score_difference))

    #human won 
    elif human_score >= 50 and computer_score < 50:
        human_score_difference = human_score - computer_score
        print("Computer lost. You won by {}".format(human_score_difference))

###############################################################################################
# Main ()#
###############################################################################################
def main():
    print_instructions()
    #set initial scores
    human_score = 0
    computer_score = 0
    input('Ready to play? (press any key) ')

    game_running = True

    while game_running:

        #total computer score 
        won_points_computer = computer_move(computer_score, human_score)
        computer_score += won_points_computer

        # Show current status for human. Calling this before human_move()
        show_current_status(computer_score, human_score)
        
        # total human score 
        won_points_human = human_move(computer_score, human_score)
        human_score += won_points_human

        #check who won 

        # Check if game is over
        if is_game_over(computer_score, human_score):
            show_final_results(computer_score, human_score)
            game_running = False 
    

if __name__ == '__main__':
    main()