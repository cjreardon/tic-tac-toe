def print_board():
    print("     |     |     ")
    print(str1)
    print("_____|_____|_____")
    print("     |     |     ")
    print(str2)
    print("_____|_____|_____")
    print("     |     |     ")
    print(str3)
    print("     |     |     ")

def is_over(arr):
    if arr[0] == "X" and arr[1] == "X" and arr[2] == "X":
        print("Player 1 wins!!!\n")
        return True
    if arr[0] == "X" and arr[4] == "X" and arr[8] == "X":
        print("Player 1 wins!!!\n")
        return True
    if arr[0] == "X" and arr[3] == "X" and arr[6] == "X":
        print("Player 1 wins!!!\n")
        return True
    if arr[3] == "X" and arr[4] == "X" and arr[5] == "X":
        print("Player 1 wins!!!\n")
        return True
    if arr[6] == "X" and arr[7] == "X" and arr[8] == "X":
        print("Player 1 wins!!!\n")
        return True    
    if arr[1] == "X" and arr[4] == "X" and arr[7] == "X":
        print("Player 1 wins!!!\n")
        return True  
    if arr[2] == "X" and arr[5] == "X" and arr[8] == "X":
        print("Player 1 wins!!!\n")
        return True    
    if arr[6] == "X" and arr[4] == "X" and arr[2] == "X":
        print("Player 1 wins!!!\n")
        return True    
    if arr[0] == "O" and arr[1] == "O" and arr[2] == "O":
        print("Player 2 wins!!!\n")
        return True
    if arr[0] == "O" and arr[4] == "O" and arr[8] == "O":
        print("Player 2 wins!!!\n")
        return True
    if arr[0] == "O" and arr[3] == "O" and arr[6] == "O":
        print("Player 2 wins!!!\n")
        return True
    if arr[3] == "O" and arr[4] == "O" and arr[5] == "O":
        print("Player 2 wins!!!\n")
        return True
    if arr[6] == "O" and arr[7] == "O" and arr[8] == "O":
        print("Player 2 wins!!!\n")
        return True    
    if arr[1] == "O" and arr[4] == "O" and arr[7] == "O":
        print("Player 2 wins!!!\n")
        return True  
    if arr[2] == "O" and arr[5] == "O" and arr[8] == "O":
        print("Player 2 wins!!!\n")
        return True    
    if arr[6] == "O" and arr[4] == "O" and arr[2] == "O":
        print("Player 2 wins!!!\n")
        return True   
    else:
        return False

arr = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
turn = 0
str1 = "  1  |  2  |  3  "
str2 = "  4  |  5  |  6  "
str3 = "  7  |  8  |  9  "

while not is_over(arr):
    turn += 1
    print_board()
    if turn % 2 == 1:
        index = input("Player 1: Where would you like to place your X? ")
        print()
        index = int(index)
        arr[index-1] = "X"
        if 0<index<4:
            str1 = str1.replace(str(index), "X")
        if 3<index<7:
            str2 = str2.replace(str(index), "X")
        if 6<index<10:
            str3 = str3.replace(str(index), "X")
    else:
        index = input("Player 2: Where would you like to place your O? ")
        print()
        index = int(index)
        arr[index-1] = "O"
        if 0<index<4:
            str1 = str1.replace(str(index), "O")
        if 3<index<7:
            str2 = str2.replace(str(index), "O")
        if 6<index<10:
            str3 = str3.replace(str(index), "O")

print()
print_board()
