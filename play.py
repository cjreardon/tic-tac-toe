import random

def print_board(arr):
    print("     |     |     ")
    print("  "+arr[0]+"  |  "+arr[1]+"  |  "+arr[2]+"   ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  "+arr[3]+"  |  "+arr[4]+"  |  "+arr[5]+"   ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  "+arr[6]+"  |  "+arr[7]+"  |  "+arr[8]+"   ")
    print("     |     |     ")


def tie_game(arr):
    return arr.count("X") == 5


def winner(char):
    print("===== " + char + " WINS!! =====")


def could_win(arr, char): # avoids extra print statements from is_over when playing computer
    if arr[0] == char and arr[1] == char and arr[2] == char:
        return True
    if arr[0] == char and arr[4] == char and arr[8] == char:
        return True
    if arr[0] == char and arr[3] == char and arr[6] == char:
        return True
    if arr[3] == char and arr[4] == char and arr[5] == char:
        return True
    if arr[6] == char and arr[7] == char and arr[8] == char:
        return True
    if arr[1] == char and arr[4] == char and arr[7] == char:
        return True
    if arr[2] == char and arr[5] == char and arr[8] == char:
        return True
    if arr[6] == char and arr[4] == char and arr[2] == char:
        return True
    else:
        return False


def is_over(arr, char):
    if arr[0] == char and arr[1] == char and arr[2] == char:
        winner(char)
        return True
    if arr[0] == char and arr[4] == char and arr[8] == char:
        winner(char)
        return True
    if arr[0] == char and arr[3] == char and arr[6] == char:
        winner(char)
        return True
    if arr[3] == char and arr[4] == char and arr[5] == char:
        winner(char)
        return True
    if arr[6] == char and arr[7] == char and arr[8] == char:
        winner(char)
        return True
    if arr[1] == char and arr[4] == char and arr[7] == char:
        winner(char)
        return True
    if arr[2] == char and arr[5] == char and arr[8] == char:
        winner(char)
        return True
    if arr[6] == char and arr[4] == char and arr[2] == char:
        winner(char)
        return True
    elif tie_game(arr):
        print("===== Tie Game!! =====")
        return True
    else:
        return False


def two_player():
    turn = 0
    arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while not is_over(arr, "X") and not is_over(arr, "O"):
        turn += 1
        print_board(arr)
        if turn % 2 == 1:
            index = input("Player 1: Where would you like to place your X? ")
            while index not in arr or index == "X" or index == "O":
                index = input("Please enter a valid move ")
            print()
            index = int(index)
            arr[index-1] = "X"
        else:
            index = input("Player 2: Where would you like to place your O? ")
            while index not in arr or index == "X" or index == "O":
                index = input("Please enter a valid move ")
            print()
            index = int(index)
            arr[index-1] = "O"
    print()
    print_board(arr)


def one_player(beatable):
    turn = 0
    arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while not is_over(arr, "X") and not is_over(arr, "O"):
        turn += 1
        print_board(arr)
        if turn % 2 == 1:
            index = input("Player 1: Where would you like to place your X? ")
            while index not in arr or index == "X" or index == "O":
                index = input("Please enter a valid move ")
            print()
            index = int(index)
            arr[index-1] = "X"
        else:
            print()
            comp = computer_move(arr, beatable)
            arr[comp] = "O"
            comp = comp + 1
            print("Computer placed an O at " + str(comp))
    print()
    print_board(arr)


def computer_move(arr, beatable):
    move_bank = [x for x, char in enumerate( #get all possible moves
        arr) if char != 'X' and char != "O"]
    if beatable == True:
        return random.choice(move_bank)
    if 4 in move_bank: #take the center
        return 4
    for char in ["O", "X"]: #take the winning move or block the human if they could win
        for i in move_bank:
            arr_copy = arr[:]
            arr_copy[i] = char
            if could_win(arr_copy, char):
                return i
    corners = []
    for i in move_bank:
        if i in [0, 2, 6, 8]:
            corners.append(i)
    if len(corners) > 0:
        return corners[0]
    edges = []
    for i in move_bank:
        if i in [1, 3, 5, 7]:
            edges.append(i)
    if len(edges) > 0:
        return edges[0]


def main():
    game_mode = input(
        "Would you like to play against a human (1), a beatable computer (2), or an unbeatable computer (3)? ")
    while(game_mode != "1" and game_mode != "2" and game_mode != "3"):
        game_mode = input("Please enter 1, 2, or 3 ")
    if int(game_mode) == 1:
        two_player()
    elif int(game_mode) == 2:
        beatable = True
        one_player(beatable)
    else:
        print("Good Luck ;)")
        beatable = False
        one_player(beatable)


main()

