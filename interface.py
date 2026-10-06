import tkinter as tk

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 600
        self.size = (8, 8)
        self.d_oval = 30
        self.b_position = (30, 30)
        self.color = []
        for i in range(self.size[0]):
            self.color.append([])
            for j in range(self.size[1]):
                self.color[-1].append('white')

        self.canva = self.init_canva()

        self.geometry(f"{self.width}x{self.height}")
        self.title("Connect 4")

    def init_canva(self):
        canva = tk.Canvas(self)
        canva.pack(fill="both", expand=tk.YES)
        canva.bind("<Configure>", self.on_resize)
        return canva

    def on_resize(self, event):

        # Update the dimension and variable creation
        self.height = event.height
        self.width = event.width

        r = min(self.width, self.height) * 0.002
        self.b_position = [(self.width - (self.d_oval + self.d_oval * 0.2) * r * self.size[0] - self.d_oval * 0.6 * r)//2,
                           (self.height - (self.d_oval + self.d_oval * 0.2) * r * self.size[1] - self.d_oval * 0.6 * r)//2]

        ## Background reset
        self.canva.create_rectangle(0, 0, self.width, self.height, fill='white')

        ## Background game board
        self.create_board()

        ## Empty cells
        self.draw_cells()

    def create_board(self):
        r = min(self.width, self.height) * 0.002  # the dynamic ratio
        d = [(self.d_oval + self.d_oval * 0.2) * r * self.size[0] + self.d_oval * 0.6 * r,
             (self.d_oval + self.d_oval * 0.2) * r * self.size[1] + self.d_oval * 0.6 * r] # rectangle dimension
        g = 30 * r # gap between rectangles corner to allow the arc
        p = self.b_position

        print(d)

        self.canva.create_rectangle(
            p[0] + g,
            p[1],
            p[0] + d[0] - g,
            p[1] + d[1],
            fill='grey',
            outline='')

        self.canva.create_rectangle(
            p[0],
            p[1] + g,
            p[0] + d[0],
            p[1] + d[1] - g,
            fill='grey',
            outline='')

        self.canva.create_oval(
            p[0] + d[0] - g * 2,
            p[1],
            p[0] + d[0],
            p[1] + g * 2,
            fill='grey',
            outline='')

        self.canva.create_oval(
            p[0],
            p[1] + d[1] - g * 2,
            p[0] + g * 2,
            p[1] + d[1],
            fill='grey',
            outline='')

        self.canva.create_oval(
            p[0] + d[0] - g * 2,
            p[1] + d[1] - g * 2,
            p[0] + d[0],
            p[1] + d[1],
            fill='grey',
            outline='')

        self.canva.create_oval(
            p[0],
            p[1],
            p[0] + g * 2,
            p[1] + g * 2,
            fill='grey',
            outline='')

    def draw_cells(self):
        r = min(self.width, self.height) * 0.002  # the dynamic ratio
        p = [self.b_position[0] + self.d_oval * 0.4 * r,
             self.b_position[1] + self.d_oval * 0.4 * r]

        d = [0, 0, self.d_oval * r, self.d_oval * r] # dimension of the ovals
        dist = self.d_oval * r * 1.2 # distance between two origin points of cells

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.canva.create_oval(p[0] + d[0] + dist * i,
                                       p[1] + d[1] + dist * j,
                                       p[0] + d[2] + dist * i,
                                       p[1] + d[3] + dist * j,
                                       fill=self.color[i][j],
                                       outline='')