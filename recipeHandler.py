import RPi.GPIO as GPIO
import time
import csv
with open('tester.csv', 'r', newline='') as csv_file:
    reader = csv.reader(line.replace('  ', ',') for line in csv_file)
    my_list = list(reader)
    for list in my_list:
        list = [int(i) for i in list]

print(list)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(37,GPIO.OUT)
GPIO.output(37,GPIO.HIGH)
time.sleep(list[0])
GPIO.output(37,GPIO.LOW)

GPIO.setup(31,GPIO.OUT)
GPIO.output(31,GPIO.HIGH)
time.sleep(list[1])
GPIO.output(31,GPIO.LOW)

GPIO.setup(32,GPIO.OUT)
GPIO.output(32,GPIO.HIGH)
time.sleep(list[2])
GPIO.output(32,GPIO.LOW)

GPIO.setup(33,GPIO.OUT)
GPIO.output(33,GPIO.HIGH)
time.sleep(list[3])
GPIO.output(33,GPIO.LOW)

GPIO.setup(35,GPIO.OUT)
GPIO.output(35,GPIO.HIGH)
time.sleep(list[4])
GPIO.output(35,GPIO.LOW)

GPIO.setup(36,GPIO.OUT)
GPIO.output(36,GPIO.HIGH)
time.sleep(list[5])
GPIO.output(36,GPIO.LOW)

GPIO.setup(37,GPIO.OUT)
GPIO.output(37,GPIO.HIGH)
time.sleep(list[6])
GPIO.output(37,GPIO.LOW)

GPIO.setup(38,GPIO.OUT)
GPIO.output(38,GPIO.HIGH)
time.sleep(list[7])
GPIO.output(38,GPIO.LOW)

GPIO.setup(39,GPIO.OUT)
GPIO.output(39,GPIO.HIGH)
time.sleep(list[8])
GPIO.output(39,GPIO.LOW)

GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.HIGH)
time.sleep(list[9])
GPIO.output(40,GPIO.LOW)
