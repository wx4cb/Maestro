import time
import servocontrol

print("Creating servo object")
servos = servocontrol.ServoController()

bearings=[-69,    -74,        38,        -70,        -2,        -18,        87,        -19,        88,        -44,        -85,        69,
            56,      48,        -71,        -8,        11,        -54,        77,        20,        -3,        8,        71,
            80,      66,        -9,        -59,        22,        30,        -78,        39,        85,        -15,        13,
            -16,    72,        -40,        -63,        -41,        -7,        64,        75,        68,        -12 ]

numelements = len(bearings)
for i in bearings:
    servos.setAngle(0, i)
    time.sleep(0.25)

servos.setAngle(0, 0)
