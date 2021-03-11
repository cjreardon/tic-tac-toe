def print_board(arr):
    print("     |     |     ")
    print("  "+arr[0][0]+"  |  "+arr[0][1]+"  |  "+arr[0][2]+"   ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  "+arr[1][0]+"  |  "+arr[1][1]+"  |  "+arr[1][2]+"   ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  "+arr[2][0]+"  |  "+arr[2][1]+"  |  "+arr[2][2]+"   ")
    print("     |     |     ")

def is_over(arr):
    if arr[0][0] == "X" and arr[0][1] == "X" and arr[0][2] == "X":
        print("Player 1 wins!!!\n")
        return True
    if arr[0][0] == "X" and arr[1][1] == "X" and arr[2][2] == "X":
        print("Player 1 wins!!!\n")
        return True
    if arr[0][0] == "X" and arr[1][0] == "X" and arr[2][0] == "X":
        print("Player 1 wins!!!\n")
        return True
    if arr[1][0] == "X" and arr[1][1] == "X" and arr[1][2] == "X":
        print("Player 1 wins!!!\n")
        return True
    if arr[2][0] == "X" and arr[2][1] == "X" and arr[2][2] == "X":
        print("Player 1 wins!!!\n")
        return True    
    if arr[0][1] == "X" and arr[1][1] == "X" and arr[2][1] == "X":
        print("Player 1 wins!!!\n")
        return True  
    if arr[0][2] == "X" and arr[1][2] == "X" and arr[2][2] == "X":
        print("Player 1 wins!!!\n")
        return True    
    if arr[2][0] == "X" and arr[1][1] == "X" and arr[0][2] == "X":
        print("Player 1 wins!!!\n")
        return True    
    if arr[0][0] == "O" and arr[0][1] == "O" and arr[0][2] == "O":
        print("Player 2 wins!!!\n")
        return True
    if arr[0][0] == "O" and arr[1][1] == "O" and arr[2][2] == "O":
        print("Player 2 wins!!!\n")
        return True
    if arr[0][0] == "O" and arr[1][0] == "O" and arr[2][0] == "O":
        print("Player 2 wins!!!\n")
        return True
    if arr[1][0] == "O" and arr[1][1] == "O" and arr[1][2] == "O":
        print("Player 2 wins!!!\n")
        return True
    if arr[2][0] == "O" and arr[2][1] == "O" and arr[2][2] == "O":
        print("Player 2 wins!!!\n")
        return True    
    if arr[0][1] == "O" and arr[1][1] == "O" and arr[2][1] == "O":
        print("Player 2 wins!!!\n")
        return True  
    if arr[0][2] == "O" and arr[1][2] == "O" and arr[2][2] == "O":
        print("Player 2 wins!!!\n")
        return True    
    if arr[2][0] == "O" and arr[1][1] == "O" and arr[0][2] == "O":
        print("Player 2 wins!!!\n")
        return True   
    else:
        return False

def get_square(index):
    if index == "1":
        row = 0
        col = 0
    if index == "2":
        row = 0
        col = 1
    if index == "3":
        row = 0
        col = 2
    if index == "4":
        row = 1
        col = 0
    if index == "5":
        row = 1
        col = 1
    if index == "6":
        row = 1
        col = 2
    if index == "7":
        row = 2
        col = 0
    if index == "8":
        row = 2
        col = 1
    if index == "9":
        row = 2
        col = 2
    return row, col


def is_taken(arr,row,col):
    while arr[row][col] == "X" or arr[row][col] == "O":
        index = input("Enter a square that is not taken. ")
        row, col = get_square(index)
    return row, col


def two_player():
    turn = 0
    arr = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    while not is_over(arr):
        turn += 1
        print_board(arr)
        if turn % 2 == 1:
            index = input("Player 1: Where would you like to place your X? ")
            print()
            row, col = get_square(index)
            row, col = is_taken(arr,row,col)
            arr[row][col] = "X"
        else:
            index = input("Player 2: Where would you like to place your O? ")
            print()
            row, col = get_square(index)
            row, col = is_taken(arr,row,col)
            arr[row][col] = "O"
    print()
    print_board(arr)

game_mode = input("Would you like to play against a human (1) or a computer (2)? ")
if int(game_mode) == 1:
    two_player()


