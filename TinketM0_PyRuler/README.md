1. Connect the Device using usb
2. Make sure it converted to Circuit python (by droping UF2 File from Circuit Python site )  
3. Install mu editor using Linux Application store  - Discover or Raspbian Recommended Software tool
4.  Open Terminal  
5.  sudo adduser $USER dialout
6.  sudo mu-editor 
7.  Select adafruit  CircuitPython
8.  IC should be automatically be selected
9.  Click on Serial
10. add code in the editor > code.py (inside IC) - 
            while True: print("hi")
            
11. Save
12. you should see the print statments in REPL


## Power Pins

BAT - This is a voltage INPUT pin, you can use it to connect a battery or other external power to the Trinket. It has a Schottkey protection diode so it is completely separate from the USB power input/output. You can put 3V-6V into this pin and it will be regulated down by the 3V regulator

USB - This is a voltage OUTPUT or INPUT pin - it is connected directly to the micro USB port +5V pin, so if you are powering over usb, this pin will give you 5V out at 500mA+. Or if you are using the Trinket as a USB host or you have a good reason, you can put 5V into this pin and it will back-power the USB port.

3V - This is the 3.3V OUTPUT pad from the voltage regulator. It can provide up to 500mA at a steady 3.3V. Good for sensors or small LEDs or other 3V devices.
GND is the common ground pin, used for logic and power. It is connected to the USB ground and the power regulator, etc. This is the pin you'll want to use for any and all ground connections


## Input/Output Pins

Next we will cover the 5 GPIO (General Purpose Input Ouput) pins! For reference you may want to also check out the datasheet-reference in the downloads section for the core ATSAMD21E18 pin. We picked pins that have a lot of capabilities.

Common to all pads:

All the GPIO pads can be used as digital inputs, digital outputs, for LEDs, buttons and switches. All pads can also be used as hardware interrupts inputs.

Each pad can provide up to ~7mA of current. Don't connect a motor or other high-power component directly to the pins! Instead, use a transistor to power the DC motor on/off

On a Trinket M0, the GPIO are 3.3V output level, and should not be used with 5V inputs. In general, most 5V devices are OK with 3.3V output though.

The five pins are completely 'free' pins, they are not used by the USB connection, LEDs, DotStar, etc so you never have to worry about the USB interface interfering with them when programming

Unique pad capabilities

Digital #0 / A2  - this is connected to PA08 on the ATSAMD21. This pin can be used as a digital I/O with selectable pullup or pulldown, analog input (use 'A2'),  PWM output, and is also used for I2C data (SDA)

Digital #1 / A0  - this is connected to PA02 on the ATSAMD21. This pin can be used as a digital I/O with selectable pullup or pulldown, capacitive touch, analog input (use 'A0'),  and true analog (10-bit DAC) output. It cannot be used as PWM output.


Digital #2 / A1  - this is connected to PA09 on the ATSAMD21. This pin can be used as a digital I/O with selectable pullup or pulldown, analog input (use 'A1'),  PWM output, and is also used for I2C clock (SCL), and hardware SPI MISO

Digital #3 / A3  - this is connected to PA07 on the ATSAMD21. This pin can be used as a digital I/O with selectable pullup or pulldown, analog input (use 'A3'),  capacitive touch, PWM output, and is also used for UART RX (Serial1 in Arduino), and hardware SPI SCK

Digital #4 / A4  - this is connected to PA06 on the ATSAMD21. This pin can be used as a digital I/O with selectable pullup or pulldown, analog input (use 'A4'),  capacitive touch, PWM output, and is also used for UART TX (Serial1 in Arduino), and hardware SPI MOSI
Other Pads!

Digital #7 - You can't see this pin but it is connected to the internal RGB DotStar data in pin

Digital #8 - You can't see this pin but it is connected to the internal RGB DotStar clock in pin

Digital #13 - You can't see this pin but it is connected to the little red status LED
Secret SWD Pads

On the bottom of the Trinket M0 you will see two small pads. These are used for our programming/test but you can use them too.