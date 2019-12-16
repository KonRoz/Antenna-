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

        # just a text label for geostationary power
        self.geostationary_label = tk.Label(self.cv, text="Geostationary Orbit", font=FONT_BUTTONS)
        self.geostationary_box = tk.Checkbutton(self.cv, variable=self.geostationary, onvalue=1, offvalue=0)
        self.geostationary_box.config(font=FONT_BUTTONS)

        # the code that comprises the drop down menu for frequency bands
        # A dictionary containing each of the standard bands
        self.choices = {'L-Band', 'S-Band', 'Ku-Band', 'Ka-Band'}
        # the initial option of the drop down meny
        self.band.set('Please Select a Frequency Band')
        # the text label prefacing the drop down menu
        self.frequency_band = tk.Label(self.cv, anchor='center', text="Select Frequency Band",
                                 font=FONT_BUTTONS)
        # initializing the drop down menu for selecting the frequency band
        self.frequency_band_drop_down = tk.OptionMenu(self.cv, self.band, *self.choices)
        # setting the font of the widget along with the background
        self.frequency_band_drop_down.config(font=FONT_BUTTONS, bg="White")
        # the button that results in the outputs being displayed --> callback: Compute
        self.input_button = tk.Button(self.cv, anchor='center', text='Enter', width=25,
                                      command=self.Compute, font=FONT_BUTTONS)
        # the button that returns to the home screen
        self.quit_button = tk.Button(self.cv, anchor='center', text='Return to Welcome', width=25, command=self.ReturntoHome,
                                     font=FONT_BUTTONS)
        # organising the widgets instantiated above within the grid object
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

        # ensuring that resizing the window does not result in a weird screen configuration
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)

        self.cv.pack(fill=BOTH, expand=YES)

    # this function is the callback function for the enter button
    # it creates an instance of the Computations class and uses it to compute the outputs that will be
    # displayed in the output window --> it also calls the OutputWindow function
    def Compute(self):
        # the Computations object needs frequency and data rate inputs
        # myDataRate and Frequency will be used to initialize the Computations object
        # Data rate and frequency are both obtained from the frequency band that the user selects
        myDataRate = None
        myFrequency = None

        # this dictionary is used to get the data rate and frequency from the user selected frequency band
        # Data rate is in mbps
        # Frequency is in GHz
        DataRateandFreqLookUp = {"L-Band": (0.400, 2),
                                 "S-Band": (2.0, 4),
                                 "Ku-Band": (6.0, 18),
                                 "Ka-Band": (40.0, 40)
                                }
        # here we retrieve the value of the drop down menu (i.e. a frequency band)
        # there is a condition statement for each of the four bands
        # the dictionary is used to assign the correct data rate and frequency to myFrequency and myDataRate
        # the first element of the tuple (i.e. data rate) is converted from mbps to bps
        # the second element of the tuple (i.e. frequency) is converted from GHz to Hz
        if self.band.get() == 'L-Band':
            myDataRate = DataRateandFreqLookUp["L-Band"][0] * (10**9)
            myFrequency = DataRateandFreqLookUp["L-Band"][1] * (10**6)

        elif self.band.get() == 'S-Band':
            myDataRate = DataRateandFreqLookUp["S-Band"][0] * (10**9)
            myFrequency = DataRateandFreqLookUp["S-Band"][1] * (10**6)

        elif self.band.get() == 'Ku-Band':
            myDataRate = DataRateandFreqLookUp["Ku-Band"][0] * (10**9)
            myFrequency = DataRateandFreqLookUp["Ku-Band"][1] * (10**6)

        elif self.band.get() == 'Ka-Band':
            myDataRate = DataRateandFreqLookUp["Ka-Band"][0] * (10**9)
            myFrequency = DataRateandFreqLookUp["Ka-Band"][1] * (10**6)
        # the case in which nothing selected --> nothing happens and no values are assigned until the user picks one
        else:
            print('ohno')

        # instantiating the computer --> orbit altitude and transmission power need to be cast from ints to floats
        # altitude is converted from km to m
        self.myComputer = Computations.Computations(1000 * float(self.altitude_box.get()), myFrequency, myDataRate, float(self.transmission_box.get()))

        # the first two inputs are calculated using the instance of Computations
        self.latency = self.myComputer.calcLatency()
        self.antenna_length = self.myComputer.calcAntennaLength()

        # based upon if geostationary orbit is selected (i.e. 1) or not (i.e. 0)
        # we have two different ways to calculate optimal dish diameter

        if self.geostationary.get() == 1:
            self.dish_diameter = self.myComputer.calcGeoStationaryDishDiameter()

        else:
            self.dish_diameter = self.myComputer.calcDishDiameter()

        # after having finished computing the inputs, OutputWindow is called
        self.OutputWindow()

    # the function that creates an instance of the Output Window
    def OutputWindow(self):
        # creating a new top level to serve as the master of the new window
        self.newWindow = tk.Toplevel(self.master)
        # Output Window is instantiated and passed the outputs that will be displayed
        self.app = OutputWindow(self.newWindow, self.dish_diameter, self.latency, self.antenna_length, float(self.altitude_box.get()))

    # the call back function for return to home
    def ReturntoHome(self):
        # the top level containing the the Input Window is destroyed
        self.master.destroy()


# the class for the window in which all the outputs are displayed
class OutputWindow:
    # the constructor which takes the values to be displayed and the master window as input
    def __init__(self, master, dish_diameter, latency, antenna_length, orbit_altitude):
        # assigning the passed output values to instance variables
        self.dish_diameter = dish_diameter
        self.latency = latency
        self.antenna_length = antenna_length
        self.orbit_altitude = orbit_altitude

        # the same code as was used above in order to display the space background
        self.bg_image = tk.PhotoImage(file=image_name)
        self.width = self.bg_image.width()
        self.height = self.bg_image.height()

        self.master = master
        self.master.title('OUTPUT WINDOW')
        self.master.geometry("%dx%d" % (self.width, self.height))

        self.frame = tk.Frame(self.master)

        self.cv = tk.Canvas(self.frame, width=self.width, height=self.height)
        self.cv.create_image(0, 0, image=self.bg_image, anchor="nw")

        # creating the widgets that will be displayed in the output window
        # the text label displaying the satellite's orbit altitude
        self.welcome_label = tk.Label(self.cv, anchor='center',
                                      text="Satellite Orbiting at %s kilometers" % self.orbit_altitude, font=FONT_TITLE)
        # the text label preceding the outputted dish diameter
        self.dish_diameter_label = tk.Label(self.cv, anchor='center', text="Optimal Dish Diameter",
                                      font=FONT_BUTTONS)
        # the text label which displays the outputted optimal dish diameter
        self.dish_diamter_output = tk.Label(self.cv, anchor='center', text="%s meters" % self.dish_diameter,
                                           font=FONT_BUTTONS)
        # the text label preceding the outputted dish latency
        self.latency_label = tk.Label(self.cv, anchor='center', text="Latency",
                                      font=FONT_BUTTONS)
        # the text label which displays the outputted latency
        self.latency_output = tk.Label(self.cv, anchor='center', text="%s seconds" % self.latency,
                                           font=FONT_BUTTONS)
        # the text label that preceding the optimal Antenna Length
        self.antenna_length_label = tk.Label(self.cv, anchor='center', text="Optimal Antenna Length",
                                      font=FONT_BUTTONS)
        # the text label that displays the optimal Antenna Length
        self.antenna_length_output = tk.Label(self.cv, anchor='center', text="%s meters" % self.antenna_length,
                                           font=FONT_BUTTONS)
        # the button which returns to the input window --> callback: quit
        self.quit_button = tk.Button(self.cv, anchor='center', text='Return to Inputs', width=25, command=self.quit,
                                     font=FONT_BUTTONS)

        # organizing all the widgets on the screen using the grid command
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

    # the callback function for the return to input window button
    def quit(self):
        # destroys the output window
        self.master.destroy()


# this is the main function of the entire program
# running the main function allows the GUI to become visible
def main():
    # root is the highest level container within the program
    # everything else within the program is contained within root
    # every tkinter program begins with a root
    root = tk.Tk()
    # here we create the first window of our application
    # passing it the root parameter dictates that it will reside within the root container
    app = WelcomeWindow(root)
    # this is how we begin the GUI
    # it continuously loops
    root.mainloop()


# this if statement check if this file is being run as main
# if this file is being run as a part of some larger program (e.g. another program creates an instance of this) then
# this statement will not run
# running main (i.e. root.mainloop()) while running a larger GUI program will result in errors
# since this we run our GUI by running GUI.py --> this if statement will be true and main() will be called
if __name__ == '__main__':
    main()








