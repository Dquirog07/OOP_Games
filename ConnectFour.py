from enum import Enum

class Piece(Enum):
    EMPTY = 0 
    YELLOW = 1
    RED = 2


class Player:
    def __init__(self, color: Piece):
        self.color = color
        self.score = None


class ConnectFour:
    def __init__(self, player1: Player, player2: Player, rows: int, columns: int):
        self.player1 = player1
        self.player2 = player2
        self.grid = [[0 for _ in range (rows)] for _ in range(columns)]
        self.winner = None

    def move(self, player: Player, column: int)->None:
        row = 0
        pos = self.grid[row][column]
        while pos == Piece.EMPTY and row < rows:
            row += 1
            pos = self.grid[row][column]            
        self.grid[row - 1][column] = player.color
        if self.checkWin((row-1, column)):
            if player.score:
                player.score += 1
                if player.score == 3:
                    print(f"{player.color} has won")
            else:
                player.score = 1
            self.resetBoard()

    def checkWin(self, position: (int, int))->bool:
        #needs to traverse the grid
        return True
    
    def resetBoard(self)->None:
        self.grid = [[0 for _ in range(len(self.grid))] for _ in range(len(self.grid[0]))]
        