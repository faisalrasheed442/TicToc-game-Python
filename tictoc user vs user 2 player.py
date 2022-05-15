import os
import re
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]


def display(bo):
    for i in range(len(bo)):
        if i % 1 == 0 and i != 0:
            print("-----")
        for j in range(len(bo)):
            if j != 0:
                print("|", end="")
            if j == 2:
                print(bo[i][j])
            else:
                print(bo[i][j], end="")


os.system("cls")


def players(bo, num):
    loop = True
    while loop:
        p1 = int(input(f"enter the postion you want to mark player p{num}\n"))
        x = r"[1-9]"
        if re.match(x, str(p1)):
            if p1 == 1 or p1 == 2 or p1 == 3:
                p1 = p1-1
                if bo[0][p1] == 1 or bo[0][p1] == 2:
                    os.system("cls")
                    display(bo)
                    print("sorry This position already filled")
                    loop = True
                else:
                    os.system("cls")
                    bo[0][p1] = num
                    display(bo)
                    loop = False
            elif p1 == 4 or p1 == 5 or p1 == 6:
                p1 = int(int(p1)-4)
                if bo[1][p1] == 1 or bo[1][p1] == 2:
                    os.system("cls")
                    display(bo)
                    print("sorry This position already filled")
                    loop = True
                else:
                    os.system("cls")
                    bo[1][p1] = num
                    display(bo)
                    loop = False
            elif p1 == 7 or p1 == 8 or p1 == 9:
                p1 = int(int(p1)-7)
                if bo[2][p1] == 1 or bo[2][p1] == 2:
                    os.system("cls")
                    display(bo)
                    print("sorry This position already filled")
                    loop = True
                else:
                    os.system("cls")
                    bo[2][p1] = num
                    display(bo)
                    loop = False
            else:
                os.system("cls")
                display(bo)
                print("wrong input")
            
            if bo[0][0] == 1 and bo[0][1] == 1 and bo[0][2] == 1 or bo[1][0] == 1 and bo[1][1] == 1 and bo[1][2] == 1 or bo[2][0] == 1 and bo[2][1] == 1 and bo[2][2] == 1 or bo[0][0] == 1 and bo[1][0] == 1 and bo[3][0] == 1 or bo[0][2] == 1 and bo[1][2] == 1 and bo[2][2] == 1 or bo[0][1] == 1 and bo[1][1] == 1 and bo[2][1] == 1 or bo[0][0] == 1 and bo[1][1] == 1 and bo[2][2] == 1 or bo[0][2] == 1 and bo[1][1] == 1 and bo[2][0] == 1:
                print("p1 won")
                loop = False
            elif bo[0][0] == 2 and bo[0][1] == 2 and bo[0][2] == 2 or bo[1][0] == 2 and bo[1][1] == 2 and bo[1][2] == 2 or bo[2][0] == 2 and bo[2][1] == 2 and bo[2][2] == 2 or bo[0][0] == 2 and bo[1][0] == 2 and bo[3][0] == 2 or bo[0][2] == 2 and bo[1][2] == 2 and bo[2][2] == 2 or bo[0][1] == 2 and bo[1][1] == 2 and bo[2][1] == 2 or bo[0][0] == 2 and bo[1][1] == 2 and bo[2][2] == 2 or bo[0][2] == 2 and bo[1][1] == 2 and bo[2][0] == 2:
                print("p2 won")
                loop = False
            else:
                return True

        else:
            os.system("cls")
            print("pleas enter a valid postion")
            loop = True


def main():
    display(board)
    x = True
    p = 1
    while x:
        if p == 1:
            x = players(board, p)
            p = 2
        elif p == 2:
            x = players(board, p)
            p = 1


main()
