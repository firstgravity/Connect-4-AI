class Game:

    def __init__(self):
        self.board = []
        self.nb_player = 2
        self.board_d = (8, 8)
        self.end = False

        for i in range(self.board_d[0]):
            self.board.append([])
            for j in range(self.board_d[1]):
                self.board[-1].append(0)

    def next_move(self):
        total_mov = 0
        mov_av = []

        for i in self.board:
            for j in i:
                if 