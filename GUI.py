import tkinter as tk

# The input window for the user


class InputWindow:

    # the constructor to which root will be passed --> the highest level window here
    def __init__(self, master):

        self.master = master
        self.frame = tk.Frame(self.master)
        self.calculateButton = tk.Button(self.frame, text='Calculate Optimal Antenna', width=25, command=self.calculate)
        self.calculateButton.pack()
        self.frame.pack()

    def calculate(self):

        self.newroot = tk.Tk()
        self.output = OutputWindow(self.newroot)
        self.master.destroy()


class OutputWindow:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.outputLabel = tk.Label(self.frame, text='output')
        self.outputLabel.pack()
        self.frame.pack()

def main():
    root = tk.Tk()
    app = InputWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()






