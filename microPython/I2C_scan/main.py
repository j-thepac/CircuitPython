

import machine
import utime
from ssd1306 import SSD1306_I2C


 
sda=machine.Pin(0)
scl=machine.Pin(1)
 
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)
print(i2c.scan())
 

 

 