import serial
import time

class ServoController:

    def __init__(self):
        self.ServoLimits = [ [600, 1600, 2400, 270],
                            [1000, 1500, 2000, 180],
                            [1000, 1500, 2000, 180],
                            [1000, 1500, 2000, 180],
                            [1000, 1500, 2000, 180],
                            [1000, 1500, 2000, 180]  ]


        usbPort = '/dev/ttyACM0'
        self.sc = serial.Serial(usbPort, timeout=1)

    def closeServo(self):
        self.sc.close()

    # Set an angle between -90 (full min to +90 full max, with 0 degrees as center position
    def setAngle(self, chan, angle):
        if angle == 0:
            ms = self.ServoLimits[chan][1]
        elif angle == -90:
            ms = self.ServoLimits[chan][0]
        elif angle == 90:
            ms = self.ServoLimits[chan][2]
        else:
            # Get new range for angle
            old_min = -90
            old_max = 90
            new_max = self.ServoLimits[chan][2]
            new_min = self.ServoLimits[chan][0]
    
            OldRange = (old_max - old_min)
            NewRange = (new_max - new_min)
    
            ms = (((angle - old_min) * NewRange) / OldRange) + new_min

        print "Servo ", chan, " to ", angle, " (", ms, ")"
        self.setPosition(chan, ms)


    # set definitive angle via maestro
    def setDefAngle(self, n, angle):
        if angle > 180 or angle <0:
           angle=90
        bud=chr(0xFF)+chr(n)+chr(byteone)
        self.sc.write(bud)

    def setPosition(self, servo, microsecs):
        microsecs = microsecs * 4
        poslo = (microsecs & 0x7f)
        poshi = (microsecs >> 7) & 0x7f
        chan  = servo &0x7f
        data =  chr(0xaa) + chr(0x0c) + chr(0x04) + chr(chan) + chr(poslo) + chr(poshi)
        self.sc.write(data)

    def getPosition(self, servo):
        chan  = servo &0x7f
        data =  chr(0xaa) + chr(0x0c) + chr(0x10) + chr(chan)
        self.sc.write(data)
        w1 = ord(self.sc.read())
        w2 = ord(self.sc.read())
        return w1, w2

    def getErrors(self):
        data =  chr(0xaa) + chr(0x0c) + chr(0x21)
        self.sc.write(data)
        w1 = ord(self.sc.read())
        w2 = ord(self.sc.read())
        return w1, w2

    def triggerScript(self, subNumber):
        data =  chr(0xaa) + chr(0x0c) + chr(0x27) + chr(0)
        self.sc.write(data)
