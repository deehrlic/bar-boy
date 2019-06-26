import sys
import os
#uncomment below when pi testing
#import RPi.GPIO as GPIO
import time

#uncomment below when pi testing
#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

class Drink:
    def __init__(self, values):
        self.values = values

    def pour(self):
        for value in self.values:
            print(value[0])
            print(value[1])
            #uncomment below when pi testing
        #    GPIO.setup(value[0])
        #    GPIO.output(value[0],GPIO.HIGH)
        #    time.sleep(value[1])
        #    GPIO.output(value[0],GPIO.LOW)

#leave below commented
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

#COSMOPOLITAN
cosmo = Drink([(36,OUNCE), (29,3*OUNCE), (37,2*OUNCE), (32,OUNCE)])
#DAQUIRI
daq = Drink([(31,2*OUNCE), (32,1.25*OUNCE), (35,OUNCE)])
#LEMON DROP
drop = Drink([(29,OUNCE), (36,.75*OUNCE), (33,.5*OUNCE)])
#MARGARITA
marg = Drink([(38,1.75*OUNCE), (36,OUNCE), (32,.75*OUNCE)])
#LONG ISLAND ICE TEA
liit = Drink([(38,.5*OUNCE), (29,.5*OUNCE), (31,.5*OUNCE), (36,.5*OUNCE), (40,.5*OUNCE), (33,OUNCE), (35,OUNCE)])
#RUM AND COKE
#rumcoke = Drink([(31,)])
#GIN TONIC
#gintonic = Drink([(40,)])
#BEAKER
beaker = Drink([(29,4*OUNCE)])

recipes = [cosmo, daq, drop, marg, liit, beaker]
names = ["cosmo", "daq", "drop", "marg", "liit", "beaker"]

print(sys.argv[1])
y = len(recipes)
for x in range(0, y):
    if names[x] == sys.argv[1]:
        recipes[x].pour()
