import math as math
import tkinter as tk

class Computations:
    height = 0

    def __init__(self, height):
        self.height = height

    #Orbital velocity of the satellite equation can be found at https://keisan.casio.com/exec/system/1224665242
    def velocity(self):
        return math.sqrt(398600.5/(6378.14 + self.height))

    #Orbital period of the satellite equation can be found at https://keisan.casio.com/exec/system/1224665242
    def period(self):
        return ((2*math.pi())*((6378.14 + self.height)/(self.velocity())))

    #chord of the satellites circumference of contact with the ground station
    def chord(self):
        return math.sqrt(2*self.height*self.height*(1-math.cos(math.radians(170))))

    #Angle from the center of the eart to the two ends of the chord
    def theta(self):
        return 2*math.asin(self.chord()/(2*(h+6378.14)))

    #Portion of the circumference of the orbit that the satellite is in contact for in kilometers.
    def s(self):
        return (h+6378.14)*self.theta()

    #Using previous functions to find the time of contact
    def getTimeOfContact(self):
        return self.s()/self.velocity()
