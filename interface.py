import tkinter as tk

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 600

        self.canva = self.init_canva((8, 8))

        self.geometry(f"{self.width}x{self.height}")
        self.title("Connect 4")

    def init_canva(self, size):
        canva = tk.Canvas(self)
        canva.pack(fill="both", expand=tk.YES)
        canva.bind("<Configure>", self.on_resize)
        return canva

    def on_resize(self, event):

        # Update the dimension
        self.height = event.height
        self.width = event.width

        ## Background reset
        self.canva.create_rectangle(0, 0, self.width, self.height, fill='white')

        ## Background game board
        self.canva.create_rectangle(30 , 30, 300, 300, fill='grey', outline='')

        ## Empty cells
        '''distance = min(self.winfo_reqwidth(), self.winfo_reqheight()) * 0.17
        initial = []
        h = [30, 30, 30 + distance * 0.7, 30 + distance * 0.7]
        for i in range(size[0]):
            for j in range(size[1]):
                canva.create_oval(h[0] + i * distance,
                                  h[1] + j * distance,
                                  h[2] + i * distance,
                                  h[3] + j * distance)'''