#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
#set GPIO Pins
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
 
def distance(trig,echo):
    # set Trigger to HIGH
    GPIO.output(trig, True)
    
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trig, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(echo) == 0:
        StartTime = time.time() 
    # save time of arrival
    while GPIO.input(echo) == 1:
        StopTime = time.time()
 
 
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            
            d = distance(GPIO_TRIGGER, GPIO_ECHO)
            d1 = distance(GPIO_TRIGGER1, GPIO_ECHO1)
          
            print ("Measured Distance = %.1f cm" % d)
            print ("Measured Distance 1 = %.1f cm" % d1)
            #print ("Measured Distance 1 = %.1f cm" % dist1)
            if 31.0 < d < 41.0 and 23.0 < d1 < 34.0:
                print("in range")
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
