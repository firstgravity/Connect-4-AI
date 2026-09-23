import tkinter as tk

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.width = 400
        self.height = 400

        self.canva = self.init_canva((8, 8))

        self.geometry("400x400")
        self.title("Connect 4")

    def init_canva(self, size):
        canva = tk.Canvas(self)
        canva.pack(fill=tk.BOTH, expand=tk.YES)

        canva.bind("<Configure>", self.on_resize)

        return canva

    def on_resize(self, event):
        self.height = event.height
        self.width = event.width
        self.canva.create_rectangle(30 , 30, 300, 300, fill='grey', outline='')
        '''distance = min(self.winfo_reqwidth(), self.winfo_reqheight()) * 0.17
        initial = []
        h = [30, 30, 30 + distance * 0.7, 30 + distance * 0.7]
        for i in range(size[0]):
            for j in range(size[1]):
                canva.create_oval(h[0] + i * distance,
                                  h[1] + j * distance,
                                  h[2] + i * distance,
                                  h[3] + j * distance)'''