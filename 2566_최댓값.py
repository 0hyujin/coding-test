import sys
input = sys.stdin.readline

board = []

for _ in range(9) :
    board.append(list(map(int, input().split())))

X = 0
Y = 0
MAX = -1

for i in range(9) :
    for j in range(9) :
        if board[i][j] > MAX :
            MAX = board[i][j]
            X = i+1
            Y = j+1

print(MAX)
print(X, Y)
