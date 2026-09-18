from tkinter import Tk

class Window(Tk):

    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("Connect 4")