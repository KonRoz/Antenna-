# File: GUI.py
# Author: Konrad Rozanski
# Email: krozansk@nd.edu
#
# This file contains the classes that comprise the GUI (graphical user interface) of the
# Antenna Selector application

# tkinter is a third party library for GUI programming in python
import tkinter as tk
from tkinter.constants import BOTH, YES
# the class used to compute the outputs for the inputted antenna specs
import Computations

# tuples containing the fonts and sizes for buttons and titles
FONT_TITLE = ("Bebas Neue", 30)
FONT_BUTTONS = ("Bebas Neue", 20)

# the background image for the application windows
image_name = "Earth.gif"


# the welcome window for the program
class WelcomeWindow:

    # the constructor for the GUI --> master is the frame that WelcomeWindow resides within
    def __init__(self, master):

        # initializing instance variables
        # creating a tkinter variable to store the background image specified above
        self.bg_image = tk.PhotoImage(file=image_name)
        # configuring image height and width --> this also serves as the height and width of the window
        self.width = self.bg_image.width()
        self.height = self.bg_image.height()

        # master is the root window for Welcome Window
        self.master = master
        self.master.title('ANTENNA SELECTOR')

        # specifying the height and width of the master window
        self.master.geometry("%dx%d" % (self.width, self.height))

        # creating a frame within which the canvas (i.e. image background) will reside
        self.frame = tk.Frame(self.master)

        # creating the canvas --> its a container that is capable of holding an image and passing it the bg image
        self.cv = tk.Canvas(self.frame, width=self.width, height=self.height)
        self.cv.create_image(0, 0, image=self.bg_image, anchor="nw")

        # creating the widgets that reside within the Welcome Window
        # Creating the header label
        self.welcome_label = tk.Label(self.cv, anchor='center', text="Welcome to the Notre Dame\n Antenna Selector",
                                      font=FONT_TITLE)
        # creating the button that brings the user to the input window --> callback function: input_window
        self.input_button = tk.Button(self.cv, anchor='center', text='Select Antenna', width=25,
                                      command=self.input_window, font=FONT_BUTTONS)
        # creating the button that allows the user to quit the application --> callback function: quit
        self.quit_button = tk.Button(self.cv, anchor='center', text='Exit', width=25, command=self.quit,
                                     font=FONT_BUTTONS)

        # configuring the widgets that were declared above
        self.welcome_label.grid(column=1, row=0, sticky='NS', padx=5, pady=5)
        self.input_button.grid(column=0, row=1, sticky='NS', padx=10, pady=10)
        self.quit_button.grid(column=2, row=1, sticky='NS', padx=10, pady=10)
        self.frame.pack(fill=BOTH, expand=YES)

        # giving each column and row the same weight so that the screen configuration remains the same upon expansion
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

        self.cv.pack(fill=BOTH, expand=YES)

    # callback functions for welcome window
    # callback function for input button --> creates instance of InputWindow
    def input_window(self):
        # tkinter does not like multiple toplevel ojects --> to create multiple top level we use tk.TopLevel
        self.newWindow = tk.Toplevel(self.master)
        self.app = InputWindow(self.newWindow)

    # call back function for quit button
    def quit(self):
        # destroys the instance of master into which the whole window is packed
        self.master.destroy()


# the input window into which the user inputs the satellite specifications
class InputWindow:

    # constructor into which the tk.TopLevel object is passed
    def __init__(self, master):

        # tk variables for checkbox widget and frequency band drop down menu
        # these need to be tk variables in order to access their values to use them in the calculations
        self.geostationary = tk.IntVar()
        self.band = tk.StringVar()

        # the outputs that will be passed to the output window
        self.dish_diameter = None
        self.latency = None
        self.antenna_length = None

        # this code is the same as in the welcome window --> it is used for the background image
        self.bg_image = tk.PhotoImage(file=image_name)
        self.width = self.bg_image.width()
        self.height = self.bg_image.height()

        self.master = master
        self.master.title('INPUT WINDOW')
        self.master.geometry("%dx%d" % (self.width, self.height))

        self.frame = tk.Frame(self.master)

        self.cv = tk.Canvas(self.frame, width=self.width, height=self.height)
        self.cv.create_image(0, 0, image=self.bg_image, anchor="nw")

        # the widgets that comprise the input window
        # just a text label titling the window
        self.welcome_label = tk.Label(self.cv, anchor='center', text="Please Input the Satelite's Specifications",
                                      font=FONT_BUTTONS)

        # just a text label prefacing the altitude input
        self.altitude = tk.Label(self.cv, anchor='center', text="Orbit Altitude (km)",
                                      font=FONT_BUTTONS)
        # the input widget for the altitude
        self.altitude_box = tk.Entry(self.cv, font=FONT_BUTTONS)
        # just a text label illustrating sample input
        self.altitude_ei = tk.Label(self.cv, anchor='center', text="e.g. 2000",
                                 font=FONT_BUTTONS)

        # input line for transmission
        # just a text label for transmission power
        self.transmission = tk.Label(self.cv, anchor='center', text="Transmission Power (W)",
                                 font=FONT_BUTTONS)
        # input widget for transmission power
        self.transmission_box = tk.Entry(self.cv, font=FONT_BUTTONS)
        # just a text label illustrating transmission power sample
        self.transmission_ei = tk.Label(self.cv, anchor='center', text="e.g. 1000",
                                    font=FONT_BUTTONS)


        self.geostationary_label = tk.Label(self.cv, text="Geostationary Orbit", font=FONT_BUTTONS)
        self.geostationary_box = tk.Checkbutton(self.cv, variable=self.geostationary, onvalue=1, offvalue=0)
        self.geostationary_box.config(font=FONT_BUTTONS)

        self.choices = {'L-Band', 'S-Band', 'Ku-Band', 'Ka-Band'}
        self.band.set('Please Select a Frequency Band')  # set the default option
        self.frequency_band = tk.Label(self.cv, anchor='center', text="Select Frequency Band",
                                 font=FONT_BUTTONS)

        self.frequency_band_drop_down = tk.OptionMenu(self.cv, self.band, *self.choices)
        self.frequency_band_drop_down.config(font=FONT_BUTTONS, bg="White")

        self.ground_station_location_box = tk.Entry(self.cv, text=' Wheaton, IL, United States ', font=FONT_BUTTONS)

        self.input_button = tk.Button(self.cv, anchor='center', text='Enter', width=25,
                                      command=self.Compute, font=FONT_BUTTONS)

        self.quit_button = tk.Button(self.cv, anchor='center', text='Return to Welcome', width=25, command=self.ReturntoHome,
                                     font=FONT_BUTTONS)

        self.welcome_label.grid(column=1, row=0, sticky='NS', padx=5, pady=50)

        self.altitude.grid(column=0, row=1, sticky='NS', padx=20, pady=20)
        self.altitude_box.grid(column=1, row=1, sticky='NS', padx=20, pady=20)
        self.altitude_ei.grid(column=2, row=1, sticky='NS', padx=20, pady=20)

        self.transmission.grid(column=0, row=2, sticky='NS', padx=20, pady=20)
        self.transmission_box.grid(column=1, row=2, sticky='NS', padx=20, pady=20)
        self.transmission_ei.grid(column=2, row=2, sticky='NS', padx=20, pady=20)

        self.frequency_band.grid(column=0, row=3, sticky='NS', padx=20, pady=20)
        self.frequency_band_drop_down.grid(column=1, row=3, sticky='NS', padx=20, pady=20)

        self.geostationary_label.grid(column=0, row=4, sticky='NS', padx=20, pady=40)
        self.geostationary_box.grid(column=1, row=4, sticky='NS', padx=20, pady=40)

        self.input_button.grid(column=0, row=5, sticky='NS', padx=20, pady=40)
        self.quit_button.grid(column=2, row=5, sticky='NS', padx=20, pady=40)

        self.frame.pack(fill=BOTH, expand=YES)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)

        self.cv.pack(fill=BOTH, expand=YES)

    def Compute(self):
        #compute frequencies from bandwidth
        #compute data rate from frequencies
        myDataRate = None
        myFrequency = None

        #Data rate is in mbps
        #Frequency is in GHz
        DataRateandFreqLookUp = {"L-Band": (0.400, 2),
                                 "S-Band": (2.0, 4),
                                 "Ku-Band": (6.0, 18),
                                 "Ka-Band": (40.0, 40)
                                }

        print(self.band.get())

        if self.band.get() == 'L-Band':
            myDataRate = DataRateandFreqLookUp["L-Band"][0] * (10**9)
            myFrequency = DataRateandFreqLookUp["L-Band"][1] * (10**6)
        elif self.band.get() == 'S-Band':
            myDataRate = DataRateandFreqLookUp["S-Band"][0] * (10 ** 9)
            myFrequency = DataRateandFreqLookUp["S-Band"][1] * (10 ** 6)
        elif self.band.get() == 'Ku-Band':
            myDataRate = DataRateandFreqLookUp["Ku-Band"][0] * (10 ** 9)
            myFrequency = DataRateandFreqLookUp["Ku-Band"][1] * (10 ** 6)
        elif self.band.get() == 'Ka-Band':
            myDataRate = DataRateandFreqLookUp["Ka-Band"][0] * (10 ** 9)
            myFrequency = DataRateandFreqLookUp["Ka-Band"][1] * (10 ** 6)
        else:
            print('ohno')

        print(myDataRate)
        print(myFrequency)

        self.myComputer = Computations.Computations(float(self.altitude_box.get()), myFrequency, myDataRate, float(self.transmission_box.get()))

        self.latency = self.myComputer.calcLatency()
        self.antenna_length = self.myComputer.calcAntennaLength()

        if self.geostationary.get() == 1:
            self.dish_diameter = self.myComputer.calcGeoStationaryDishDiameter()
            print(self.dish_diameter)
            print(self.latency)
        else:
            self.dish_diameter = self.myComputer.calcDishDiameter()
            print(self.dish_diameter)
            print(self.latency)

        self.OutputWindow()

    def OutputWindow(self):

        self.newWindow = tk.Toplevel(self.master)
        self.app = OutputWindow(self.newWindow, self.dish_diameter, self.latency, self.antenna_length, float(self.altitude_box.get()))

    def ReturntoHome(self):

        self.master.destroy()


class OutputWindow:

    def __init__(self, master, dish_diameter, latency, antenna_length, orbit_altitude):
        self.dish_diameter = dish_diameter
        self.latency = latency
        self.antenna_length = antenna_length
        self.orbit_altitude = orbit_altitude

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
                                      text="Satellite Orbiting at %s meters" % self.orbit_altitude, font=FONT_TITLE)

        self.dish_diameter_label = tk.Label(self.cv, anchor='center', text="Optimal Dish Diameter",
                                      font=FONT_BUTTONS)

        self.dish_diamter_output = tk.Label(self.cv, anchor='center', text="%s meters" % self.dish_diameter,
                                           font=FONT_BUTTONS)

        self.latency_label = tk.Label(self.cv, anchor='center', text="Latency",
                                      font=FONT_BUTTONS)

        self.latency_output = tk.Label(self.cv, anchor='center', text="%s seconds" % self.latency,
                                           font=FONT_BUTTONS)

        self.antenna_length_label = tk.Label(self.cv, anchor='center', text="Optimal Antenna Length",
                                      font=FONT_BUTTONS)

        self.antenna_length_output = tk.Label(self.cv, anchor='center', text="%s meters" % self.antenna_length,
                                           font=FONT_BUTTONS)

        self.quit_button = tk.Button(self.cv, anchor='center', text='Return to Inputs', width=25, command=self.quit,
                                     font=FONT_BUTTONS)

        self.welcome_label.grid(column=2, row=0, sticky='NS', padx=5, pady=50)

        self.dish_diameter_label.grid(column=1, row=1, sticky='NS', padx=20, pady=20)
        self.dish_diamter_output.grid(column=3, row=1, sticky='NS', padx=20, pady=20)

        self.latency_label.grid(column=1, row=2, sticky='NS', padx=20, pady=20)
        self.latency_output.grid(column=3, row=2, sticky='NS', padx=20, pady=20)

        self.antenna_length_label.grid(column=1, row=3, sticky='NS', padx=20, pady=20)
        self.antenna_length_output.grid(column=3, row=3, sticky='NS', padx=20, pady=20)

        self.quit_button.grid(column=2, row=4, sticky='NS', padx=20, pady=50)

        self.frame.pack(fill=BOTH, expand=YES)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

        self.cv.pack(fill=BOTH, expand=YES)

    def quit(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = WelcomeWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()






