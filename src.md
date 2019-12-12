'''
#!/usr/bin/env pybricks-micropython
"""
gary-the-dancing-machine
"""
# a bunch of things that just let you use the buttons and sensors and such
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here

# Names of notes and frequencies
R = 001.0000
ASh = 466.1600
B = 493.8833
DSh = 622.2500
CSh = 554.3700
GSh = 415.3000

# Telling the computer where the motors and sensors are connected to it
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
sensor = TouchSensor(Port.S1)

# A function that tells the robot what notes to play and for how long
def sing (Hz = [B,R,B,R,ASh,ASh,ASh,R,DSh,DSh,DSh,CSh,CSh,B,R,B,R,ASh,ASh,ASh,R,DSh,DSh,DSh,CSh,CSh,GSh,R,GSh,R,ASh,ASh,ASh,R,B,B,B,ASh,ASh,GSh,R,GSh,R,ASh,ASh,ASh,R,B,B,B,ASh,ASh], d = [.5,.2,.5,.2,.5,.5,.5,.2,.5,.5,.5,.5,.5,.5,.2,.5,.2,.5,.5,.5,.2,.5,.5,.5,.5,.5,.5,.2,.5,.2,.5,.5,.5,.2,.5,.5,.5,.5,.5,.5,.2,.5,.2,.5,.5,.5,.2,.5,.5,.5,.5,.5]):
    for f in range(0,len(Hz)):
        if Hz[f] == 1:
            wait(250*d[f])
        else:
            brick.sound.beep(Hz[f], 250*d[f])
        wait(125)

# Loops program so that it doesn't shut off after one use
while True:
    # Looking for a button press, if it finds it it runs the motors and plays a song, otherwise...
    if sensor.pressed():
        motor_a.run(500)
        motor_b.run(500)
        # Calling the 'sing' function from earlier, this is when that function actually runs
        sing()
    #...It stops the motors and goes back to waiting
    else:
        motor_a.stop(Stop.BRAKE)
        motor_b.stop(Stop.BRAKE)
'''
