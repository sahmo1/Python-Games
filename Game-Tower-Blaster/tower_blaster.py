import random 

def setup_bricks():
    '''
    run this function once at the beginning of the game.
    create a main pile with 60 integers and empty discard pile 
    return this as a tuple 
    '''
    setup_main_pile = [bricks for bricks in range(1,61)]
    setup_discard = []

    return (setup_main_pile, setup_discard)


def shuffle_bricks(bricks):
    '''
    Shuffle this function at the start of the game. 
    Function does not return anything
    '''
    random.shuffle(bricks)

def check_bricks(main_pile, discard):
    '''
    checking main pile to make sure any bricks are in there. pick the top card from the main pile and turn that to discard pile 
    '''
    if len(main_pile) == 0:
        shuffle_bricks(discard)

        for pile in discard:
            main_pile.append(pile)

        discard.clear()
        discard.insert(0, main_pile.pop(0))

def check_tower_blaster(tower):
    '''
    check stability and return boolean values. 
    '''
    if tower == sorted(tower):
        return True
    else:
        return False 


def get_top_brick(brick_pile):
    '''
    Remove and return the top brick from any given pile of bricks. This can be the main_pile, the discard pile, or your tower or the computer's tower. In short, remove and return the first element of any given list. 

    It is used at the start of game play for dealing bricks. This function will also be used during each player’s turn to take the top brick from either the discarded brick pile or from the main pile. 

    Note: Brick piles are vertically oriented structures, with the top having index 0.
    This function must return an integer.
    '''
    return int(brick_pile.pop(0))


def deal_initial_bricks(main_pile):
    '''
    dealing initial 10 bricks for computer and player. Computer always first then the player
    Returns a tuple 
    '''
    computer_bricks = []
    player_bricks = []
    
    for brick in range(10):
        computer_bricks.insert(0, main_pile.pop(0))       
        player_bricks.insert(0, main_pile.pop(0))     

    return (computer_bricks, player_bricks)


def add_brick_to_discard(brick, discard):
    '''
    Add the given brick (represented as an integer) to the top of the given discard pile (which is a list)
    
    '''
    discard.insert(0, brick)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    '''
    Find the given brick to be replaced (represented by an integer) in the given tower and replace it with the given new brick.

    Check and make sure that the given brick to be replaced is truly a brick in the given tower.

    The given brick to be replaced then gets put on top of the given discard pile. 

    Return True if the given brick is replaced, otherwise return False.
    
    '''
    if brick_to_be_replaced in tower:
        brick_index = tower.index(brick_to_be_replaced)
        tower.pop(brick_index)
        tower.insert(brick_index, new_brick) 
        discard.insert(0, brick_to_be_replaced)

        return True 
    else:
        return False


def computer_play(tower, main_pile, discard):
    '''
    My computer's strategy. I first checked the first brick in computer_bricks and compare that value to the average. 
    '''
    print("\n----------It's Computer's Turn----------") 
    if tower[0] <= average:
        if discard[0] <= average:
            find_and_replace( get_top_brick(discard), tower[0], tower, discard )
            print("Computer picked from the discard pile.")
        else:
            top_brick_main_pile = get_top_brick(main_pile)
            if top_brick_main_pile <= average:
                find_and_replace(top_brick_main_pile, tower[0], tower, discard)
                print("Computer picked from the mystery pile.")
            else:
                add_brick_to_discard(top_brick_main_pile, discard)
                print("Computer rejected from the mystery pile.")
    else:
        get_discard_top_brick = get_top_brick(discard)
        print("Computer played")

        #starting to compare the second brick to the brick next one and so on to find out the replacement
        index = 2
        # Find Index thats lower
        while tower[index - 1] < tower[index]:
            index += 1
            if index == 8:
                break
        
        maxTowerIndex = max(tower[:index])
        if get_discard_top_brick < maxTowerIndex:
            x = 0
            while True:
                if get_discard_top_brick < tower[x]:
                    find_and_replace(get_discard_top_brick, tower[x], tower, discard)
                    print("Computer replaced a brick")
                    break
                x += 1
        else:
            find_and_replace(get_discard_top_brick, tower[index], tower, discard)
            print("Computer replaced a brick")
        

    
    
             
def human_play(tower, main_pile, discard):
    '''
    A function for a player to compete with computer  
    '''
    
    print("\n----------It's Your Turn----------") 
    

    #top brick from the discard pile is this. 
    print( 'Your Tower {}'.format(tower) )
    print( 'The top brick on the discard pile is {}'.format(discard[0]) )
    choosing_pile_message = input("Type 'D' to take the discard brick, 'M' for a mystery brick\n")
    
    if choosing_pile_message.lower() == 'm':
         #if you choose M then get the first brick in the pile 
        # print("You picked {} from the Main Pile".format(main_pile[0]))
        print("The mystery brick is {}".format(main_pile[0]))
        deciding_message = input("Do you want to use this brick?(Enter 'y' or 'n')\n")
        
        if deciding_message.lower() == 'y':
            #where you want to replace this?
            message= int(input("Which number do you want to replace?\n"))
            find_and_replace(main_pile[0], message, tower, discard)
            # print("You replaced {} with {}".format(message, get_top_brick(main_pile)))
            
            print("Your new tower: {}".format(tower))
            return
        
        else:
            #if you see the brick from the main pile and you dont want it then put this brick into the discard pile 
            add_brick_to_discard(main_pile[0], discard)
            # print("You did not choose your brick from main pile.")
            print("Your new tower: {}".format(tower))
            return
       
        
    elif choosing_pile_message.lower() == "d":
        # print("You picked from the Discard Pile, which is {}".format(discard[0]))
        #need to ask where you want to replace your brick 
        message = int(input('Which brick on your tower you want to replace?\n'))
        find_and_replace(get_top_brick(discard), message, tower, discard) 
        print("Your new tower: {}".format(tower))
        return
    
         
def instruction():

    message = 'Welcome to Tower Blaster!\n----------Instruction----------\nTower Blaster is a game where you are competing with a computer to line bricks in an ascending order. Each number represents a width of the brick. You and the computer will receive 10 bricks initially. Each turn, you will get to decide whether you want to choose a brick from a main pile or discard pile, or skip your turn. You can only see your brick from the discard pile. But if you choose a brick from a discard pile, you must take it. However, if you choose a brick from a main pile, although you cannot see the brick, you can decide whether you want to take it or not. The first person to line your brick in an ascending order wins.'

    print(message)


def setup_average(main_pile):
    '''
    calculating the average of the main_pile 
    '''
    avg_value = round(sum(main_pile) / len(main_pile) / 2)
    return avg_value


def main():
    
    global average

    instruction()
    input("Ready to play? Press Enter\n")

    game_running = True  
    
    main_pile, discard = setup_bricks()

    average = setup_average(main_pile)

    shuffle_bricks(main_pile)

    
    computer_bricks, player_bricks = deal_initial_bricks(main_pile)
    # The top brick of the main pile is turned over to begin the discarded brick pile
    add_brick_to_discard(main_pile.pop(0), discard)  
    

    while game_running:

        # Check your bricks
        check_bricks(main_pile, discard)

        #computer plays first 
        computer_play(computer_bricks, main_pile, discard)

        #Human plays second
        human_play(player_bricks, main_pile, discard)


        #check to make sure who won and ends the game 
        if check_tower_blaster(computer_bricks):
            print("Computer won!")
             #end game
            game_running = False 
        
        elif check_tower_blaster(player_bricks):
            print("You won!")
            #end game
            game_running = False 


    

if __name__ == '__main__':
    main()