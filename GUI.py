import tkinter as tk
from tkinter.constants import BOTH,YES
import Computations as Computer

FONT_TITLE = ("Bebas Neue", 30)
FONT_BUTTONS = ("Bebas Neue", 20)

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

        self.welcome_label = tk.Label(self.cv, anchor='center', text="Welcome to the Notre Dame\n Antenna Selector",
                                      font=FONT_TITLE)
        self.input_button = tk.Button(self.cv, anchor='center', text='Select Antenna', width=25,
                                      command=self.input_window, font=FONT_BUTTONS)
        self.quit_button = tk.Button(self.cv, anchor='center', text='Exit', width=25, command=self.quit,
                                     font=FONT_BUTTONS)

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
        self.satAltitude = tk.IntVar()

        self.bg_image = tk.PhotoImage(file=image_name)
        self.width = self.bg_image.width()
        self.height = self.bg_image.height()

        self.master = master
        self.master.title('INPUT WINDOW')
        self.master.geometry("%dx%d" % (self.width, self.height))

        self.frame = tk.Frame(self.master)

        self.cv = tk.Canvas(self.frame, width=self.width, height=self.height)
        self.cv.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.welcome_label = tk.Label(self.cv, anchor='center', text="Please Input the Satelite's Specifications",
                                      font=FONT_TITLE)

        self.altitude = tk.Label(self.cv, anchor='center', text="Orbit Altitude",
                                      font=FONT_TITLE)

        self.altitude_box = tk.Entry(self.cv, text=' 3000000000 ', font=FONT_BUTTONS)

        self.altitude_ei = tk.Label(self.cv, anchor='center', text="e.g. 200000000 m",
                                 font=FONT_TITLE)

        self.ground_station_location = tk.Label(self.cv, anchor='center', text="Ground Station Location",
                                 font=FONT_TITLE)

        self.ground_station_location_box = tk.Entry(self.cv, text=' Wheaton, IL, United States ', font=FONT_BUTTONS)

        self.ground_station_location_ei = tk.Label(self.cv, anchor='center', text="e.g. Notre Dame, IN, United States",
                                                   font=FONT_TITLE)

        self.input_button = tk.Button(self.cv, anchor='center', text='Enter', width=25,
                                      command=self.getAltitude, font=FONT_BUTTONS)

        self.quit_button = tk.Button(self.cv, anchor='center', text='Return to Welcome', width=25, command=self.ReturntoHome,
                                     font=FONT_BUTTONS)

        self.welcome_label.grid(column=1, row=0, sticky='NS', padx=5, pady=5)
        self.altitude.grid(column=0, row=1, sticky='NS', padx=5, pady=5)
        self.altitude_box.grid(column=1, row=1, sticky='NS', padx=5, pady=5)
        self.altitude_ei.grid(column=3, row=1, sticky='NS', padx=5, pady=5)
        self.ground_station_location.grid(column=0, row=2, sticky='NS', padx=5, pady=5)
        self.ground_station_location_box.grid(column=1, row=2, sticky='NS', padx=5, pady=5)
        self.ground_station_location_ei.grid(column=3, row=2, sticky='NS', padx=5, pady=5)
        self.input_button.grid(column=0, row=3, sticky='NS', padx=10, pady=10)
        self.quit_button.grid(column=2, row=3, sticky='NS', padx=10, pady=10)
        self.frame.pack(fill=BOTH, expand=YES)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

        self.cv.pack(fill=BOTH, expand=YES)

    def getAltitude(self):
        self.altitude_value = self.altitude_box.get()
        self.OutputWindow()

    def OutputWindow(self):

        self.newWindow = tk.Toplevel(self.master)
        self.app = OutputWindow(self.newWindow, self.altitude_value)

    def ReturntoHome(self):

        self.master.destroy()


class OutputWindow:

    def __init__(self, master, myAltitude, DishDiameter):
        self.myAltitude = myAltitude
        self.DishDiameter = DishDiameter

        self.bg_image = tk.PhotoImage(file=image_name)
        self.width = self.bg_image.width()
        self.height = self.bg_image.height()

        self.master = master
        self.master.title('OUTPUT WINDOW')
        self.master.geometry("%dx%d" % (self.width, self.height))

        self.frame = tk.Frame(self.master)

        self.cv = tk.Canvas(self.frame, width=self.width, height=self.height)
        self.cv.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.welcome_label = tk.Label(self.cv, anchor='center',
                                      text="Satellite Orbiting at %s meters" % (str(self.myAltitude)), font=FONT_TITLE)

        self.preface_label = tk.Label(self.cv, anchor='center', text="Optimal Dish Diameter",
                                      font=FONT_TITLE)

        self.dish_diamter_label = tk.Label(self.cv, anchor='center', text="%s meters" % (str(self.DishDiameter)),
                                           font=FONT_TITLE)

        self.welcome_label.grid(column=2, row=0, sticky='NS', padx=5, pady=5)
        self.preface_label.grid(column=1, row=1, sticky='NS', padx=5, pady=5)
        self.dish_diamter_label.grid(column=3, row=1, sticky='NS', padx=5, pady=5)
        self.frame.pack(fill=BOTH, expand=YES)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

        self.cv.pack(fill=BOTH, expand=YES)

    def outputWindow(self):
        self.calculateStuff()
        self.newWindow = tk.Toplevel(self.master)
        self.app = OutputWindow(self.newWindow, self.myAltitude, self.DishDiameter)

    def calculateStuff(self):
        self.myComputer.height = float(self.myAltitude)
        self.DishDiameter = float(self.myComputer.getDiameter())

    def quit(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = WelcomeWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()






