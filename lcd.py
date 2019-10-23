from RPLCD import i2c 
from time import *
import subprocess

lcdmode = 'i2c'
cols = 16
rows = 2
charmap = 'A00'
i2c_expander = 'PCF8574'
address = 0x27
port = 1

lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,cols=cols,rows=rows)



lcd.backlight_enabled = True 

lcd.write_string(subprocess.run(['hostname', '-I'],stdout = subprocess.PIPE).stdout.decode('utf-8')[:10])

sleep(5)

lcd.backlight_enabled = False
lcd.close(clear=True)


