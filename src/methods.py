# imports

import sys
import time

sys.setrecursionlimit(1000000000)
# class


board=[
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]
rowMaskValues = []
columnMaskValues = []
gridMaskValues = []

boardCopy = [r[:] for r in board]

# Masking Functions


def isValid(row, col):
    if row >= 9 or col >= 9:
        return False
    elif row < 0 or col < 0:
        return False

    return True


def nextEmptySpace(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return (-1, -1)


def isValidNumber(row, col, num):
    if isValid(row, col):
        if rowMaskValues[row] & 1 << (num - 1):
            return False
        elif columnMaskValues[col] & 1 << (num - 1):
            return False
        elif gridMaskValues[(row // 3) * 3 + col // 3] & 1 << (num - 1):
            return False
        return True
    return False


def rowMask(row, arr):
    mask = 0
    for r in arr[row]:
        if r > 0:
            mask += 1 << r - 1
    return mask


def columnMask(col, arr):
    mask = 0
    for r in range(9):
        if (arr[r][col]) > 0:
            mask += 1 << arr[r][col] - 1
    return mask


def gridMask(gridIndex, arr):
    mask = 0
    if gridIndex < 3:
        for i in range(3):
            for j in range(3):
                if arr[i][gridIndex * 3 + j] > 0:
                    mask += 1 << arr[i][gridIndex * 3 + j] - 1
    elif gridIndex < 6:
        for i in range(3, 6):
            for j in range(3):
                if arr[i][(gridIndex - 3) * 3 + j] > 0:
                    mask += 1 << arr[i][(gridIndex - 3) * 3 + j] - 1
    else:
        for i in range(6, 9):
            for j in range(3):
                if arr[i][(gridIndex - 6) * 3 + j] > 0:
                    mask += 1 << arr[i][(gridIndex - 6) * 3 + j] - 1

    return mask


def updateMask(arr):
    global rowMaskValues
    rowMaskValues = []
    global columnMaskValues
    columnMaskValues = []
    global gridMaskValues
    gridMaskValues = []
    for i in range(9):
        rowMaskValues.append(rowMask(i, arr))
        columnMaskValues.append(columnMask(i, arr))
        gridMaskValues.append(gridMask(i, arr))


def displayMask():
    print(rowMaskValues)
    print(columnMaskValues)
    print(gridMaskValues)


def displaySudoku(board):
    for x in board:
        for y in x:
            print(y, end=" ")
        print()


# Solver
print("Solving...")

def solve(tboard):
    updateMask(tboard)
    row, col = nextEmptySpace(tboard)
    if row == -1:
        return tboard

    for i in range(1, 10):
        updateMask(tboard)
        if isValidNumber(row, col, i):
            tboard[row][col] = i
            result = solve(tboard)
            if result != [[]] and result is not None:
                return result
            tboard[row][col] = 0
    return [[]]


def solveSudoku(board):
    startTime = time.time()
    sboard = solve(board)
    endTime = time.time()
    displaySudoku(sboard)
    print(f"Solved in : {endTime-startTime} seconds")


solveSudoku(boardCopy)
