import sys
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Drink:
    def __init__(self, values)
        self.values = values

    def pour(self):
        for value in self.values:
            print value[0]
            print value[1]
            GPIO.setup(value[0])
            GPIO.output(value[0],GPIO.HIGH)
            time.sleep(value[1])
            GPIO.output(value[0],GPIO.LOW)

#Pin Numbers:
#Vodka           29
#(Light) Rum     31
#Lime Juice      32
#Lemon Juice     33
#Simple Syrup    35
#Triple Sec      36
#Cranberry       37
#Tequila         38
#Gin             40

#HOW LONG AN OUNCE TAKES TO POUR
OUNCE = 0.0

cosmo = new Drink([(36,OUNCE), (29,3*OUNCE), (37,2*OUNCE), (32,OUNCE)])
daq = new Drink([(31,2*OUNCE), (32,1.25*OUNCE), (35,OUNCE)])
