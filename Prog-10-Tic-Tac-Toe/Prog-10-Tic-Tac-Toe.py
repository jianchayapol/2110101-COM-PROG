# 2110101 Computer Programming

# Prog-10: Tic-Tac-Toe
# 6330085821 

import random
                     
def main():
    N = int(input('Board size = '))
    board = [["-"]*N for j in range(N)]
    end = False
    print_board(board)
    while(not end):
        print("========== Player Turn ==========")
        player_input(board)
        print_board(board)
        check = check_win(board)
        if(check != "-"):
            if(check == "D"):
                print("############# DRAW ##############")
            else:
                print("\\(^o^)/     YOU WIN !!!     \\(^o^)/")
            break
        print("======== Computer Turn ==========")
        com_fill(board)
        print_board(board)
        check = check_win(board)
        if(check != "-"):
            if(check == "D"):
                print("############# DRAW ##############")
            else:
                print("(;-;)    YOU LOSE!!!    (;-;)")
            break
    print("Game has ended, thanks for playing :D")

def com_fill(board):
    N = len(board)
    new_board = [[x for x in y] for y in board]
    for i in range(N):
        for j in range(N):
            if board[i][j] == "-":
                new_board[i][j] = "O"
                if(check_win(new_board) == "O"):
                    board[i][j] = "O"
                    return
                new_board[i][j] = "X"
                if(check_win(new_board) == "X"):
                    board[i][j] = "O"
                    return
                new_board[i][j] = "-"
    while True:
        i = random.randint(0, N-1)
        j = random.randint(0, N-1)
        if board[i][j] == "-":
            board[i][j] = "O"
            break

def print_board(board):
    N = len(board)
    print(" "*3 , end = "")
    for i in range(N):
        print((str(i)+ " "*(3))[:3], end = "")
    print()
    for row in range(N):
        print((str(row)+ " "*(3))[:3], end = "")
        for col in range(N):
            print(board[row][col], end = "    ")
        print()

def player_input(board):
    f = False
    while not f:
        try:
            row = int(input("row = "))
            col = int(input("col = "))
            f = fill(board, row, col)
            if (not f):
                print("!!! You can't fill that spot !!!")
                print("---try again---")
        except:
            print("!!! Invalid Input !!!")
            print("---try again---")


#------------------------------------------

def fill(board, r , c):
    if r>=0 and c>=0:
        if board[r][c] == '-':
            board[r][c] = 'X'
            return True
        else:
            return False


def check_win(board):
    check = ''
    column = [[board[j][i] for j in range(len(board))] for i in range(len(board))]
    diag1 = []
    diag2 = []
    n = 0
    for i in range(len(board)):
        if board[i].count('O') == len(board) or column[i].count('O') == len(column):
            return 'O'
        if board[i].count('X') == len(board) or column[i].count('X') == len(column):  
            return 'X'
        if ('O' not in board[i] or 'X' not in board[i]) or ('O' not in column[i] or 'X' not in column[i]):
            n+=1
        diag1.append(board[i][i])
        diag2.append(board[i][len(board)-1-i])
    if diag1.count('O') == len(diag1) or diag2.count('O') == len(diag2):
        return 'O'
    if diag1.count('X') == len(diag1) or diag2.count('X') == len(diag2):
        return 'X'
    if 'O' not in diag1 or 'X' not in diag1 or 'O' not in diag2 or 'X' not in diag2:
        n+=1
    if n == 0:
        return 'D'
    return '-'
        

#------------------------------------------

main()