from machine import Pin, I2C, UART
import utime
import pmsa003

from ssd1306 import SSD1306_I2C

WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height

#i2c = I2C(0)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
i2c = I2C(0,sda=Pin(20),scl=Pin(21))
print(i2c)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

oled.fill(0)

# Methods
# ---------------------------------------------------------------------------
def read_value(sensor):
    oled.fill(0)
    oled.text("A",120,0)
    """Read a sensor value and store it in the database."""
    # Read the value from the sensor.
    reading = sensor.read()
    #now = datetime.utcnow()
    
    print(" pm10: {:d} pm25: {:d} pm100: {:d}" .format(reading.pm10_cf1, reading.pm25_cf1, reading.pm100_cf1))
    oled.text("PM1.0= {:2d}".format(reading.pm10_cf1),5,5)
    oled.show()
    oled.text("PM2.5= {:2d}".format(reading.pm25_cf1),5,15)
    oled.show()
    oled.text("PM10.0= {:2d}".format(reading.pm100_cf1),5,25)
    oled.show()
    oled.text("S",120,0)
    oled.show()
  
  
sensor = pmsa003.Sensor("0")    
utime.sleep(2)    
        
while True:
        read_value(sensor)
        utime.sleep(2) #delay of two sec

