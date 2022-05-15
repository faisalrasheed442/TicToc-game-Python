
import re
import random
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
pre=[]
def display_board(board):
    for x in range(len(board)):
        if x!=0:
            print("_____")
        for y in range(len(board[x])):
            if y!=0:
                print("|",end="")
            if y==2:
                print(board[x][y])
            else:
                print(board[x][y],end="")

def computer_postion():
    
    while True:
        x=random.randint(1,9)
        if x in pre:
            continue
        else:
            pre.append(x)
            return x
            

def check_postion(postion,player_number):
    if postion>=1 and postion<=3:
        postion=postion-1
        if board[0][postion]!=0:
            return True
        else:
            board[0][postion]=player_number
            return False
    elif postion>3 and postion<=6:
        if postion<=5:
            postion=int(round(postion/3)-1)
            if board[1][postion]!=0:
                return True
            else:
                board[1][postion]=player_number
                return False
        else:
            postion=int(postion/3)
            if board[1][postion]!=0:
                return True
            else:
                board[1][postion]=player_number
                return False
    elif postion>6 and postion<=9:
        if postion<=8:
            postion=int(round(postion/3)-2)
            if board[2][postion]!=0:
                return True
            else:
                board[2][postion]=player_number
                return False
        else:
            postion=int(postion/3-1)
            if board[2][postion]!=0:
                return True
            else:
                board[2][postion]=player_number
                return False

def check_board_value(board):
    draw=False
    for x in range(len(board)):
        if 0 in board[x]:
            draw=True
    return draw

def players(board,player_number):
    loop=True
    correct_postion=r"[1-9]"
    while loop:
        if player_number=='X':
            postion=int(input("Pick an open slot: \t"))
        else:
            postion=computer_postion()
        if re.match(correct_postion, str(postion)):
            check=check_postion(postion,player_number)
            if check:
                display_board(board)
                print("sorry This position already filled")
                loop = True
            else:
                display_board(board)
                loop = False
            if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X' or board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
                print("You win! Game Over!")
                loop = False
                return False
            elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O' or board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O' or board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O' or board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or board[0][2] == 'O' and board[1][2] == 2 and board[2][2] == 'O' or board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' or board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
                print("Computer win! Game Over!")
                loop = False
                return False
            else:
                check=check_board_value(board)
                if not check:
                    print("The Match is draw no one Win")
                    exit()
                else:
                    return True
        else:
                print("pleas enter a valid postion")
                loop = True

def main():
    print("You go first. Your letter is X.")
    display_board(board)
    x = True
    p = 'X'
    while x:
        
        if p == 'X':
            p = 'O'
            x = players(board, 'X')
        else:
            x = players(board, 'O')
            p = 'X'
        print('\n')
main()