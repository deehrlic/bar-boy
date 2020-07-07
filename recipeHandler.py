import RPi.GPIO as GPIO
import time, sys, csv, os, random
from threading import Thread
import distance, sys

#ADD DISTANCE HERE 
#IF DIST GOOD KEEP GO
#ELSE AFTER 5sec EXIT



GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#################
#Ounce constant, the amount of time in seconds it takes to pour 1oz (30ml)
OUNCE = 5
#################

def pour(pin, value):
    print(pin, value)
    print("\n")
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(value)
    GPIO.output(pin,GPIO.LOW)

threads = []

#Check if distance is valid
GPIO_TRIGGER = 7
GPIO_ECHO = 11
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#set GPIO Pins
GPIO_TRIGGER1 = 13
GPIO_ECHO1 = 15
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)

#if distance.checkDistance(GPIO_TRIGGER, GPIO_ECHO, GPIO_TRIGGER1, GPIO_ECHO1) == True:
    
if sys.argv[1] in ["hurricane", "lagoon", "mistake", "glue", "cleaner"]:
    print(sys.argv[1])
    d0 = str(sys.argv[1]) + "0"
    d1 = str(sys.argv[1]) + "1"
    cmd0 = 'python3 recipeHandler.py ' + d0
    cmd1 = 'python3 recipeHandler.py ' + d1
    os.system(cmd0)
    os.system(cmd1)
    if sys.argv[1] in ["mistake", "cleaner", "hurricane"]:
        d2 = str(sys.argv[1]) + "2"
        cmd2 = 'python3 recipeHandler.py ' + d2
        os.system(cmd2)
        
    
 #check if passed matches a file in recipe dir, and converts input to list of ints
full = sys.argv[1] + ".csv"
if any(fname == full for fname in os.listdir('./recipes')):
    print(full)
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
        print("success")
                

else:
    print("recipe no exist")
    sys.exit(-1)





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
