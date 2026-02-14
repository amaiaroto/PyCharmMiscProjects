class Board:
    def __init__(self, grid_cx_ry: tuple[int, int], fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", pg=None):
        self.columns, self.rows = grid_cx_ry
        self.pg = pg
        self.turn = 1
        self.state = self.readFEN(fen)

    def readFEN(self, fen):
        """
        :param fen: fen string, see https://www.chess.com/terms/fen-chess for explanation
        :return:
        """
        state = {}
        rp = 8
        rows = fen.split('/')
        # meta = {'r': BlackRook, 'n': BlackKnight, 'b': BlackBishop, 'q': BlackQueen,
        #         'k', BlackKing, 'p':BlackPawn, 'R': WhiteRook, 'N': WhiteKnight, 'B': WhiteBishop,
        # 'Q': WhiteQueen, 'K': WhiteKing, 'P': WhitePawn}
        for row in rows:
            cp = 1
            for col in row:
                current_column = state.get(chr(96 + rp))
                if current_column is None:
                    current_column = {k: None for k in range(1, 9)}
                    state[chr(96 + rp)] = current_column
                if col.isdigit():
                    cp += int(col)
                else:
                    current_column[cp] = col
                    cp += 1
            rp -= 1
        return state

    def printASCII(self):
        board = ""

        for r in range(8, 0, -1):
            ar = ""
            for c in range(1, 9):
                ar += self.state[chr(96 + r)][c] if self.state[chr(96 + r)][c] is not None else '.'

            board += ar + "\n"

        board = ' ' + ' '.join(list(board))
        print(board)
        return board

    def draw(self):
        ...


if __name__ == '__main__':
    Board((0, 0)).printASCII()
