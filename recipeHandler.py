#import RPi.GPIO as GPIO
import time, sys, csv, os, random
from threading import Thread

#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

#################
#Ounce constant, the amount of time in seconds it takes to pour 1oz (30ml)
OUNCE = 3
#################

def pour(pin, value):
    print(pin, value)
    print("\n")
    #GPIO.setup(pin,GPIO.OUT)
    #GPIO.output(pin,GPIO.HIGH)
    #time.sleep(value)
    #GPIO.output(pin,GPIO.LOW)

threads = []

#check if passed matches a file in recipe dir, and converts input to list of ints
full = sys.argv[1] + ".csv"
if any(fname == full for fname in os.listdir('./recipes')):
    with open('recipes/' + sys.argv[1] + '.csv', 'r', newline='') as csv_file:
        reader = csv.reader(line.replace('  ', ',') for line in csv_file)
        my_list = list(reader)
        for list in my_list:
            for i in list:
                if "OUNCE" in i:
                    list[list.index(i)] = round(OUNCE * float(i[:3]), 2)
                elif "RANDOM" in i:
                    list[list.index(i)] = round(random.random() * 5, 2)
                else:
                    list[list.index(i)] = int(i)
        pins = my_list[0]
        values = my_list[1]
        print(pins, values)
        for pin in pins:
            t = Thread(target=pour, args=(pin,values[pins.index(pin)]))
            threads.append(t)
            t.start()
        for t in threads:
                t.join()
                

else:
    raise Exception('Recipe does not exist: {}'.format(full))




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
