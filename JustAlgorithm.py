board = [[8,0,0,0,0,0,0,0,0],
         [0,0,3,6,0,0,0,0,0],
         [0,7,0,0,9,0,2,0,0],
         [0,5,0,0,0,7,0,0,0],
         [0,0,0,0,4,5,7,0,0],
         [0,0,0,1,0,0,0,3,0],
         [0,0,1,0,0,0,0,6,8],
         [0,0,8,5,0,0,0,1,0],
         [0,9,0,0,0,0,4,0,0]]

def isPossible(sx, sy, n):
    sPx = (sx//3)*3
    sPy = (sy//3)*3
    for y in range(0,9):
        if board[y][sx] == n:
            return False
    for x in range(0,9):
        if board[sy][x] == n:
            return False
    for y in range(0,3):
        for x in range(0,3):
            if board[sPy+y][sPx+x] == n:
                return False
    return True
def solve():
    global board
    for y in range(9) :
        for x in range(9) :
            if board[y][x] == 0 :
                for n in range(1,10):
                    if isPossible(x,y,n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
    print(board)
