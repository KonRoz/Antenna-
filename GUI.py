import tkinter as tk

class InputWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.outputButton = tk.Button(self.frame, text = 'New Window', width = 25,
                        command = self.new_window)

