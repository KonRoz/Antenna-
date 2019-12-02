import tkinter as tk
from tkinter.constants import BOTH,YES

FONT_TITLE = ("Mincho", 30, "italic")
FONT_BUTTONS = ("Bebas Neue", 20, "italic")

image_name = "Earth.gif"


class WelcomeWindow:

    def __init__(self, master):
        self.bg_image = tk.PhotoImage(file=image_name)
        self.width = self.bg_image.width()
        self.height = self.bg_image.height()

        self.master = master
        self.master.title('ANTENNA SELECTOR')
        self.master.geometry("%dx%d" % (self.width, self.height))

        self.frame = tk.Frame(self.master)

        self.cv = tk.Canvas(self.frame, width=self.width, height=self.height)
        self.cv.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.welcome_label = tk.Label(self.cv, anchor='center', text="Welcome to the Notre Dame\n Antenna Selector", font=FONT_TITLE)
        self.input_button = tk.Button(self.cv, anchor='center', text='Select Antenna', width=25, command=self.input_window, font=FONT_BUTTONS)
        self.quit_button = tk.Button(self.cv, anchor='center', text='Exit', width=25, command=self.quit, font=FONT_BUTTONS)

        self.welcome_label.grid(column=1, row=0, sticky='NS', padx=5, pady=5)
        self.input_button.grid(column=0, row=1, sticky='NS', padx=10, pady=10)
        self.quit_button.grid(column=2, row=1, sticky='NS', padx=10, pady=10)
        self.frame.pack(fill=BOTH, expand=YES)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

        self.cv.pack(fill=BOTH, expand=YES)


    def input_window(self):

        self.newWindow = tk.Toplevel(self.master)
        self.app = InputWindow(self.newWindow)

    def quit(self):

        self.master.destroy()


class InputWindow:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = WelcomeWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()






