import tkinter as tk

class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        self.canva = self.init_canva((8, 8))

        self.geometry("400x400")
        self.title("Connect 4")

    def init_canva(self, size):
        canva = tk.Canvas(self)
        canva.pack(fill="both", expand=True)

        canva.create_rectangle(30, 30, 300, 300, fill='grey', outline='')

        distance = min(canva.winfo_reqwidth(), canva.winfo_reqheight()) * 0.17
        h = [30, 30, 30 + distance * 0.7, 30 + distance * 0.7]
        for i in range(size[0]):
            for j in range(size[1]):
                canva.create_oval(h[0] + i * distance, h[1] + j * distance, h[2] + i * distance, h[3] + j * distance)

        return canva