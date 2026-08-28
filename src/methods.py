# class


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
    rowMaskValues = []
    columnMaskValues = []
    gridMaskValues = []


# Masking Functions
s = Sudoku()


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
    return -1


def isValidNumber(row, col, num):
    if isValid(row, col):
        if s.rowMaskValues[row] & num:
            return False
        elif s.columnMaskValues[col] & num:
            return False
        elif s.gridMaskValues[(row // 3) * 3 + col // 3] & num:
            return False
        return True
    return False


def rowMask(row):
    mask = 0
    for r in s.board[row]:
        if r > 0:
            mask += 1 << r - 1
    return mask


def columnMask(col):
    mask = 0
    for r in range(9):
        if (s.board[r][col]) > 0:
            mask += 1 << s.board[r][col] - 1
    return mask


def gridMask(gridIndex):
    mask = 0
    if gridIndex < 3:
        for i in range(3):
            for j in range(3):
                if s.board[i][gridIndex * 3 + j] > 0:
                    mask += 1 << s.board[i][gridIndex * 3 + j] - 1
    elif gridIndex < 6:
        for i in range(3, 6):
            for j in range(3):
                if s.board[i][(gridIndex - 3) * 3 + j] > 0:
                    mask += 1 << s.board[i][(gridIndex - 3) * 3 + j] - 1
    else:
        for i in range(6, 9):
            for j in range(3):
                if s.board[i][(gridIndex - 6) * 3 + j] > 0:
                    mask += 1 << s.board[i][(gridIndex - 6) * 3 + j] - 1

    return mask


def getShadow():
    pass


def initializeMask():
    for i in range(9):
        s.rowMaskValues.append(rowMask(i))
        s.columnMaskValues.append(columnMask(i))
        s.gridMaskValues.append(gridMask(i))


def displayMask():
    print(s.rowMaskValues)
    print(s.columnMaskValues)
    print(s.gridMaskValues)


def displaySudoku(board):
    for x in board:
        for y in x:
            print(y, end=" ")
    print()
