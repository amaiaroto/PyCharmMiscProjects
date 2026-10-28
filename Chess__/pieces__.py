import runpy
from enum import Enum
import json

class Color(Enum):
    white = 1
    black = 2

class Board:
    def __init__(self,file="startingboard__.json"):
        with open(file,"r") as f:
            b=json.loads(f.read())


        self.board = {}
        #loop over the map and replace all values with text_pos call to the approriate class

        location = ''
        color = None
        legal_moves = []
        letter = ''

class Piece:
    def __init__(self,name,color,row,col):
        self.name=name
        self.color=color
        self.row=row
        self.col=col


class Pawn(Piece):
    def __init__(self,color,row,col):
        super().__init__("P",color,row,col)


    def move(self,state):
        valid=[]
        if state.turns==1:
            if self.color==Color.black:
                if self.row<7:
                    valid.append((self.col,self.row+1))
                    valid.append((self.col,self.row+2))
                if state.get(self.row-1,self.col+1):
                    valid.append((self.col+1, self.row -1))
                if state.get(self.row-1,self.col-1):
                    valid.append((self.col-1, self.row -1))


class Knight(Piece):
    # def __init_subclass__(#):
        ##.string = 'N'

    def __move__(self):
        ...  # display gray circles


class Bishop(Piece):
    # def __init_subclass__(#):
        ##.string = 'B'

    def __move__(self):
        ...  # display gray circles


class Rook(Piece):
    # def __init_subclass__(#):
        ##.string = 'R'

    def __move__(self):
        ...  # display gray circles


class Queen(Piece):
    # def __init_subclass__(#):
        ##.string = 'Q'

    def __move__(self):
        ...  # display gray circles


class King(Piece):
    # def __init_subclass__(#):
        ##.string = 'K'

    def __move__(self):
        ...  # display gray circles

# Rules:
#   Ke1-e3 is illegal
#   Knight is marked N
#   Always make sure to add + after your move to indicate check
#   Checkmate is #

if __name__ == '__main__':
    runpy.run_path('chess__.py')
