#class 
from colorsys import rgb_to_yiq
class Sudoku:
    board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


#Masking Functions
s = Sudoku()
def rowMask(row):
    mask = 0
    for r in s.board[row]:
        if r > 0:
            mask += 1 << r-1
    return mask
                
def columnMask(col):
    mask = 0
    for r in range(9):
        if(s.board[r][col])>0:
            mask += 1 << s.board[r][col] -1
    return mask
                       
                       
def gridMask():
    pass

def getShadow():
    pass 

def displaySudoku(board):
    for x in board:
        for y in x:
            print(y, end=" ")
    print()
