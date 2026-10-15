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

        if self.end:
            return []

        for i in range(self.board_d[0]):
            for j in range(self.board_d[1]):
                if not(j in [x["pos"][1] for x in mov_av]):
                    if self.board[j][i] == 0:
                        mov_av.append({"player":None, "position":(i, j)})
                    else:
                        total_mov += 1

        player = total_mov % self.nb_player
        for i in mov_av:
            i["player"] = player

        return mov_av

    def win(self, player):
        for i in range(self.board_d[0]):
            count = 0
            for j in range(self.board_d[1]-1):
                if count < 4 :
                    if self.board[i][j] == self.board[i][j+1]:
                        count += 1
                    else :
                        count = 0
                else :
                    return 1 if player == self.board[i][j+1] else -1
        