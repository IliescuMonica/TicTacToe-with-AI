import random
import time

human = "X"
AI = "O"

board = [" " for _ in range(9)]
def make_board(board):
    delimitation='------'
    bar ="|"
    print(
        f"{bar.join(board[0:3])}\n"
        f"{delimitation}\n"
        f"{bar.join(board[3:6])}\n"
        f"{delimitation}\n"
        f"{bar.join(board[6:9])}"
    )

def check_win(board,player):
    if (
            board[0] == board[1] == board[2] == player or
            board[3] == board[4] == board[5] == player or
            board[6] == board[7] == board[8] == player or
            board[0] == board[3] == board[6] == player or
            board[1] == board[4] == board[7] == player or
            board[2] == board[5] == board[8] == player or
            board[0] == board[4] == board[8] == player or
            board[2] == board[4] == board[6] == player):
        return False , f"Game over!The winner is player'{player}'."
    elif " " not in board:
            return False , "Draw!Game over!"
    else:
        return True , ""

def check_combination(board,player):
    if (
            board[0] == board[1] == board[2] == player or
            board[3] == board[4] == board[5] == player or
            board[6] == board[7] == board[8] == player or
            board[0] == board[3] == board[6] == player or
            board[1] == board[4] == board[7] == player or
            board[2] == board[5] == board[8] == player or
            board[0] == board[4] == board[8] == player or
            board[2] == board[4] == board[6] == player):
        return True
    else:
        return False

# AI moves
def ai_player(board,player):

    if player == "X":
        opponent = "O"
    else:
        opponent = "X"

    possible_move = []
    corners=(0, 2, 6, 8)
    for i in range(9):
        if board[i]==" ":
            possible_move.append(i)

    # check for a win
    for move in possible_move:
        test_board = board.copy()
        test_board[move] = player
        if check_combination(test_board, player):
            return move

    # block opponent
    for move in possible_move:
        test_board = board.copy()
        test_board[move] = opponent
        if check_combination(test_board, opponent):
            return move

    #check center
    if board[4] ==" ":
        move = 4
        return move

    #check corners
    for corner in corners:
        if board[corner]==" ":
            move=corner
            return move

    # random move
    empty_positions = []
    for i in range(9):
            if board[i]==" ":
                empty_positions.append(i)
    return random.choice(empty_positions)

def game():
    make_board(board)
    game_on = True

    while game_on:
        #human move
        user_input = int(input("Enter your desired position(between 1 and 9):")) - 1
        if 0<=user_input<9 and board[user_input]==" ":
                board[user_input]= human
                make_board(board)
                game_on, message = check_win(board, human)
                #AI move
                if game_on:
                    move=ai_player(board,AI)
                    time.sleep(2)
                    board[move] = AI
                    game_on, message = check_win(board, AI)
                    print("AI has chosen its move.")
                    make_board(board)
        else:
            print("Invalid input")

    print(message)

game()




