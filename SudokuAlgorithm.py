from tkinter import *
from time import *

#main window
root = Tk()
root.minsize(350,305)
root.maxsize(350,305)
board = [[8,0,0,0,0,0,0,0,0],
         [0,0,3,6,0,0,0,0,0],
         [0,7,0,0,9,0,2,0,0],
         [0,5,0,0,0,7,0,0,0],
         [0,0,0,0,4,5,7,0,0],
         [0,0,0,1,0,0,0,3,0],
         [0,0,1,0,0,0,0,6,8],
         [0,0,8,5,0,0,0,1,0],
         [0,9,0,0,0,0,4,0,0]]
objectBoard =[[0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0]]

class square():
    def __init__(self,x,y,t,root,color):
        self.tbox = Label(root,text = str(t), height=2, width=5,borderwidth = 1, relief = "solid", bg = color)
        self.tbox.grid(row = y, column = x)
    def changeColor(self,color):
        self.tbox.config(bg = color)
    def changeNum(self,t):
        self.tbox.configure(text = str(t))

def buildBoard(board):
    for y in range(9):
        for x in range(9):
            if objectBoard[y][x] != 0:
                objectBoard[y][x] = square(x,y,(board[y][x]),root, objectBoard[y][x].tbox.cget("bg"))
            else:
                objectBoard[y][x] = square(x,y,(board[y][x]),root,"#ffffff")


def isPossible(x, y, n):
    cx = (x//3)*3
    cy = (y//3)*3
    for yl in range(9):
        if board[yl][x] == n:
            return False
    for xl in range(9):
        if board[y][xl] == n:
            return False
    for yl in range(3):
        for xl in range(3):
            if board[yl+cy][xl+cx] == n:
                return False
    return True
def solve():
    global objectBoard
    global board
    for y in range(9) :
        for x in range(9) :
            if board[y][x] == 0 :
                objectBoard[y][x].changeColor("blue")
                buildBoard(board)
                root.update()
                for n in range(1,10):
                    if isPossible(x,y,n):
                        board[y][x] = n
                        print("("+ str(x) + ","+str(y)+"): " + str(n))
                        objectBoard[y][x].changeColor("green")
                        buildBoard(board)
                        root.update()
                        solve()
                        board[y][x] = 0
                        objectBoard[y][x].changeColor("#ffffff")
                        buildBoard(board)
                        root.update()
                return
    print(board)

buildBoard(board)
solve()
root.mainloop()
