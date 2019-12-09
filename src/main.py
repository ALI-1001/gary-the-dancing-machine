#!/usr/bin/env pybricks-micropython
"""
gary-the-dancing-machine
"""
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
sensor = TouchSensor(Port.S1)
while True:
    if sensor.pressed():
        motor_a.run(500)
        motor_b.run(500)
    else:
        motor_a.stop(Stop.BRAKE)
        motor_b.stop(Stop.BRAKE)
        
