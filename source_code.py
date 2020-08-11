import random
#global variables
board=["_", "_", "_",
       "_", "_", "_",
       "_", "_", "_"]

Winner=None


game_stop=False

def check_row():
   # print("checking rows")
    global board, Winner
    if board[0]==board[1]==board[2]!="_":
        Winner=board[0]
    if board[3]==board[4]==board[5]!="_":
        Winner=board[4]
    if board[6]==board[7]==board[8]!="_":
        Winner=board[8]

def check_column():
    #print("checking column")
    global board, Winner
    if board[0]==board[3]==board[6]!="_":
        Winner=board[0]
    if board[1]==board[4]==board[7]!="_":
        Winner=board[4]
    if board[2]==board[5]==board[8]!="_":
        Winner=board[8]
    
def check_diagonal():
    #print("checking diagonal")
    global board, Winner
    if board[0]==board[4]==board[8]!="_":
        Winner=board[0]
    if board[2]==board[4]==board[6]!="_":
        Winner=board[4]

#4
def check_win():
    global Winner
    
    check_row()
    if Winner:
        return 
    else:
        check_column()
        if Winner:
            return 
        else:
            check_diagonal()
            
#5
def check_tie():
    global board
    
    if "_" in board:
        return False
    else:
        return True

#6
def shuffle_player(current_player):
    if current_player=="X":
        return "O"
    else:
        return "X"

#3
def handle_player(position, current_player):
    global Winner, game_stop
    board[position]=current_player
    
    check_win()
    if not Winner:
        booli=check_tie()
        if booli:
            display_board()
            print("Its a Tie:( ")
            game_stop=True
            return
        
    else:
        display_board()
        print(Winner+" won:) ")
        game_stop=True
        return
    current_player=shuffle_player(current_player)
    return current_player
    
            
#2      
def display_board():
    global board
    
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])
        
        
        
        
#1
def play_game(current_player):
    global board
    
    display_board()
    print(current_player+" play: ")
    
    position=int(input("choose a number between 1-9: "))-1
    valid=False
    while not valid:
        while position not in range(9):
            print("invalid number, try again")
            position=int(input("choose a number between 1-9: "))-1
        if board[position]!="_":
            print("this position is already occupied, try again.")
            position=int(input("choose a number between 1-9: "))-1
        else:
            valid=True
            
    current_player=handle_player(position, current_player)
    return current_player

if __name__=="__main__":
    current_player=random.choice(["X", "O"])
    
    while not game_stop:
        current_player=play_game(current_player)

    
