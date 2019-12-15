import tkinter as tk
from tkinter.constants import BOTH,YES
import Computations

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

        #inputs
        self.geostationary = tk.IntVar()
        self.band = tk.StringVar()

        #Outputs
        self.dish_diameter = None
        self.latency = None
        self.antenna_length = None

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
                                      font=FONT_BUTTONS)

        self.altitude = tk.Label(self.cv, anchor='center', text="Orbit Altitude",
                                      font=FONT_BUTTONS)

        self.altitude_box = tk.Entry(self.cv, font=FONT_BUTTONS)

        self.altitude_ei = tk.Label(self.cv, anchor='center', text="e.g. 200000000 m",
                                 font=FONT_BUTTONS)

        self.transmission = tk.Label(self.cv, anchor='center', text="Transmission Power",
                                 font=FONT_BUTTONS)

        self.transmission_box = tk.Entry(self.cv, font=FONT_BUTTONS)

        self.transmission_ei = tk.Label(self.cv, anchor='center', text="e.g. 200000000 Watts",
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






