import math as math

class Computations:
    def __init__(self, altitude, frequency, dataRate, power):
        self.frequency = frequency#Carrier frequency in hz
        self.altitude = altitude#Altitude in meters
        self.dataRate = dataRate #data rate in bits/s
        self.power = power#power of the ground station transmitter

        #constants
        self.speedOfLight = 3*10**8
        self.rainAttenuation = 6
        self.efficiency = .6
        self.shannonsLimit = -1.6
        self.frequencyGHz = self.frequency/(10**9)
        self.powerDb = 10 * math.log(self.power)
        self.earthRadius = 6371000

        #GeoStationary Orbit Gain equations
        self.wavelength = self.speedOfLight / self.frequency

        #antennaGain = 27000/beamwidth^2
        #beamwidth = 21/(frequency * dishDiameter)
        #Ideal equation shannonsLimit = reciverGain + antennaGain + powerDb - spaceloss - rainAttenuation
        #solving for dish dishDiameter

        #Latency Calculation
        def calcLatency(self):
            latency = self.altitude/(self.speedOfLight)
            return self.latency

        def calcAntennaLength(self):
            antennaLength = self.wavelength / 2
            return antennaLength


        def calcGeoStationaryDishDiameter(self):
            spaceLoss = 147.55 - 20*math.log(self.altitude) - 20*math.log(self.frequencyGhz)
            recieverGain = (math.pi**2*self.dataRate**2*self.efficiency)/self.wavelength
            tempVal = self.shannonsLimit - recieverGain - self.powerDb + spaceLoss + self.rainAttenuation
            #21/(frequency * dishDiameter) = e^(tempVal/10)
            self.geoStationaryDishDiameter = ((math.exp(tempVal/10))**-1)*(21/self.frequencyGHz)
            return self.geoStationaryDishDiameter

        #Asynchronous orbit calculations
        #averaging the values of the altitude across half a pass in order to determine space loss
        def calcDishDiameter(self):
            altitudeSamples = []
            for i in range(84):
                altitudeSamples.append(self.altitudeSample(self, i + 5))
            altitudeSamples.append(altitude)
            averageAltitude = 0
            for i in range(85):
                averageAltitude = altitudeSamples[i] + averageAltitude
            averageAltitude = averageAltitude/85

            spaceLoss = 147.55 - 20*math.log(averageAltitude) - 20*math.log(self.frequencyGhz)
            recieverGain =(math.pi**2)*((self.dataRate**2).efficiency)/self.wavelength
            tempVal = self.shannonsLimit - recieverGain - self.powerDb + spaceLoss + self.rainAttenuation
            #21/(frequency * dishDiameter) = e^(tempVal/10)
            self.geoStationaryDishDiameter = ((math.exp(tempVal/10))**-1)*(21/self.frequencyGHz)
            return self.geoStationaryDishDiameter


        #Solving an angle side side triangle using law of sines
        def altitudeSample(self, theta):
            angle2 = math.asin((math.sin(math.degrees(theta+5+90)))/(self.earthRadius+self.altitude)*self.earthRadius)
            angle3 = 180 - (theta + 90 + 5) - angle2
            sample = math.sin(angle3)*(self.earthRadius+self.altitude)/math.sin(theta + 90 + 5)
            return sample
