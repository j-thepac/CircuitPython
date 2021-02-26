from machine import Pin,I2C
from ssd1306 imort SSD1306_I2C

i2c =I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
oled=SSD1306_I2C(128,64,i2c)

oled.fill(0)
oled.text("Hello",0,0)
oled.show()
