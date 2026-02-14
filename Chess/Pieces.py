class Piece:
    def __init__(self, name: str = 'pawn', color: str | str = 'white', pos: str = ''):
        self.piece = name
        self.color = color
        self.square = pos

    def move(self, new_sqaure):
        self.square = new_sqaure
