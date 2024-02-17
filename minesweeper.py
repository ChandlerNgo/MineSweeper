import random
# class board:
#   int row
#   int column
#   int bombs
#   tile[][] board_data
#   createBoard()
#   isSolved()
#   printBoard()

# class tile:
#   bool isCovered
#   int value

class Board:
    def __init__(self,rows,columns,bombs):
        self.rows = rows
        self.columns = columns
        self.bombs = bombs
        self.board_data = []
        self.cursor_row = 0
        self.cursor_column = 0

        # base board
        for row in range(rows):
            self.board_data.append([])
            for column in range(columns):
                self.board_data[row].append(Tile(False, 0, False))
        while(bombs > 0):
            column = random.randint(0,columns-1)
            row = random.randint(0,rows-1)
            if(self.getTileValue(row,column) != "B"):
                self.setTileValue(row,column,"B")
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        # i and j != 0
                        if (row + i) < self.rows and (row + i) >= 0 and (column + j) < self.columns and (column + j) >= 0 and self.getTileValue(row+i,column+j) != "B":
                            self.setTileValue(row+i,column+j,self.getTileValue(row+i,column+j) + 1)
                bombs -= 1
        
    def printBoard(self):
        for row in range(self.rows):
            line = ""
            line2 = ""
            for column in range(self.columns):
                if self.getCovered(row,column) == True:
                    line += "   "
                else:
                    line += (" " + str(self.getTileValue(row,column)) + " ")
                if self.cursor_row == row and self.cursor_column == column:
                    line2 += " ^ "
                else:
                    line2 += "   "
            print(line)
            print(line2)
    
    def getTile(self, row, column):
        return self.board_data[row][column]
    
    def getFlagged(self, row, column):
        return self.board_data[row][column].isFlagged

    def getTileValue(self, row, column):
        return self.board_data[row][column].value
    
    def getCovered(self, row, column):
        return self.board_data[row][column].isCovered
    
    def setTile(self, row, column, tile):
        self.board_data[row][column] = tile
    
    def setFlagged(self, row, column):
        self.board_data[row][column].isFlagged = not self.board_data[row][column].isFlagged

    def setTileValue(self, row, column, value):
        self.board_data[row][column].value = value
    
    def setCovered(self, row, column):
        self.board_data[row][column].isCovered = not self.board_data[row][column].isCovered
    
    def moveCursor(self,action):
        if action == "left":
            if self.cursor_column != 0:
                self.cursor_column -= 1
                return 1
            else:
                return None
        if action == "up":
            if self.cursor_row != 0:
                self.cursor_row -= 1
                return 1
            else:
                return None
        if action == "down":
            if self.cursor_row < self.rows:
                self.cursor_row += 1
                return 1
            else:
                return None
        if action == "right":
            if self.cursor_column < self.columns:
                self.cursor_column += 1
                return 1
            else:
                return None
    
        
class Tile:
    def __init__(self, isCovered, value, isFlagged):
        self.isCovered = isCovered
        self.value = value
        self.isFlagged = isFlagged

    def flag(self):
        self.isFlagged = not self.isFlagged


board = Board(5,5,10)
board.printBoard()
print()
print(board.moveCursor("right"))
board.printBoard()