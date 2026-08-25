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

boardBinary = []

for x in board:
    for y in x:
        print(y, end=" ")
    print()

for x in board:
    temp = []
    i = 0
    for y in x:
        if y > 0:
            temp.append(1)
        else:
            temp.append(0)
    boardBinary.append(temp)

print()
print()
for x in boardBinary:
    for y in x:
        print(y, end=" ")
    print()

