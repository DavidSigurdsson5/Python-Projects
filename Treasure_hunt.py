import math
import random

# Initilization
BOARD_HEIGHT = 10
BOARD_WIDTH = 40

treasure_row = random.randint(0,BOARD_HEIGHT)
treasure_col = random.randint(0,BOARD_WIDTH)

monster_row = random.randint(0,BOARD_HEIGHT)
monster_col = random.randint(0,BOARD_WIDTH)

# Make sure that the player doesn't start in the same place as the monster
player_row = monster_row
player_col = monster_col
while player_row == monster_row and player_col == monster_col:
    player_row = random.randint(0,BOARD_HEIGHT)
    player_col = random.randint(0,BOARD_WIDTH)

# Controlling variables, i.e. the state of the game
player_is_alive = True
treasure_is_hidden = True

# Main game loop
while player_is_alive and treasure_is_hidden:
    # Print the gameboard (but keep the treasure hidden)
    print('-'*(BOARD_WIDTH+2))
    for row in range(BOARD_HEIGHT):
        print('|', end='')
        for col in range(BOARD_WIDTH):
            if row == monster_row and col == monster_col:
                print('M', end='')
            elif row == treasure_row and col == treasure_col:
                print('.', end='')
            elif row == player_row and col == player_col:
                print('o', end='')
            else:
                print('.', end='')
        print('|')    
    print('-'*(BOARD_WIDTH+2))

    ## Player turn
    player_move = input('Select your move [(w)up (s)down (a)left (d)right (h)hint]: ')

    # Move the player or give a treasure hint
    if player_move == 'd':
        player_col = player_col + 1
        if player_col >= BOARD_WIDTH:
            player_col = 0   
    elif player_move == 'a':
        player_col = player_col - 1
        if player_col < 0:
            player_col = BOARD_WIDTH-1  
    elif player_move == 's':
        player_row = player_row + 1
        if player_row >= BOARD_HEIGHT:
            player_row = 0   
    elif player_move == 'w':
        player_row = player_row - 1
        if player_row < 0:
            player_row = BOARD_HEIGHT-1 
    elif player_move == 'h':
        print('Treasure direction: ', end='')
        if player_row < treasure_row:
            print('S', end='')
        if player_row > treasure_row:
            print('N', end='')
        if player_col < treasure_col:
            print('E', end='')
        if player_col > treasure_col:
            print('W', end='')
        print()

    ## Move the monster

    # Initialization before the move
    min_distance = math.sqrt(BOARD_WIDTH**2 + BOARD_HEIGHT**2)
    best_monster_move_col = monster_col
    best_monster_move_row = monster_row

    # Find the square that is closest to the player
    for tmp_row in range(monster_row-1, monster_row+2):
        for tmp_col in range(monster_col-1, monster_col+2):
            current_dist = math.sqrt( (player_col - tmp_col)**2 + (player_row - tmp_row)**2 )
            if current_dist < min_distance:
                min_distance = current_dist
                best_monster_move_row = tmp_row
                best_monster_move_col = tmp_col

    monster_col = best_monster_move_col
    monster_row = best_monster_move_row

    ## Update the game situation

    # Check if monster has caught us
    if monster_row == player_row and monster_col == player_col:
        player_is_alive = False

    # Check if treasure is found
    if treasure_col == player_col and treasure_row == player_row:
        treasure_is_hidden = False

# Print the game board, showing the treasure
print('-'*(BOARD_WIDTH+2))
for row in range(BOARD_HEIGHT):
    print('|', end='')
    for col in range(BOARD_WIDTH):
        if row == monster_row and col == monster_col:
            print('M', end='')
        elif row == treasure_row and col == treasure_col:
            print('T', end='')
        elif row == player_row and col == player_col:
            print('o', end='')
        else:
            print('.', end='')
    print('|')    
print('-'*(BOARD_WIDTH+2))

# Print the outcome of the game
if player_is_alive == False:
    print('Sorry, the monster caught you!')
elif treasure_is_hidden == False:
    print('Congratulations, you found the treasure!!!')
print('---------------------')

