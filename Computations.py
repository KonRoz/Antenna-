import math as math

#This class uses the assumptions that the orbit passes directly above the ground station,
#is spherical, and the ground station is a fixed station and has a downlink and uplink
#frequency of 1 GHz
#The antennas will need to be a high gain directional antenna
#The antenna will operate at the ideal, which is possible for 1/2 wavelength dipole antennas 100% efficiency
#Given that the operating frequency is 1 GHz the recommended data rate is 400KB/s
class Computations:
    height = 0

    def __init__(self, height=None):
        if height is None:
            self.height = None
        else:
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
        return 2*math.asin(self.chord()/(2*(self.height+6378.14)))

    #Portion of the circumference of the orbit that the satellite is in contact for in kilometers.
    def s(self):
        return (self.height+6378.14)*self.theta()

    #Using previous functions to find the time of contact
    def getTimeOfContact(self):
        return self.s()/self.velocity()

    #This will be the space loss in dB for signal, 0.29979 is the wavelength of a 1 gigahertz signal
    #The calculation will be 1.76(A decent gain for a directive antennahttp://www.antenna-theory.com/basics/gain.php) = Reciever gain + antenna gain - spaceloss
    def spaceLoss(self):
        return ((0.299792458)*(0.299792458))/(4*math.pi*self.s())

    def receiverGain(self):
        return ((math.pi*math.pi)*(400000*400000)*.95)/((0.299792458)*(0.299792458))

    def getDiameter(self):
        return (21*math.sqrt(self.spaceLoss()+1.76-self.receiverGain()))**(-1)/1000000000
