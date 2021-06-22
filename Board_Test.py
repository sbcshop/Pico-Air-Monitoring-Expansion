from machine import Pin, I2C, UART
import time
import pmsa003

from ssd1306 import SSD1306_I2C


WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height

#i2c = I2C(0)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
i2c = I2C(0, freq=399361, scl=Pin(21), sda=Pin(20))
print(i2c)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config


oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

oled.fill(0)

# Methods
# ---------------------------------------------------------------------------
def read_value(sensor):
    oled.fill(0)
    """Read a sensor value and store it in the database."""
    # Read the value from the sensor.
    reading = sensor.read()
    #now = datetime.utcnow()
    print(" pm10: {:8d} pm25: {:8d} pm100: {:8d}".format(reading.pm10_cf1, reading.pm25_cf1, reading.pm100_cf1))
    oled.text("PM1.0= {:2d}".format(reading.pm10_cf1),5,5)
    oled.text("PM2.5= {:2d}".format(reading.pm25_cf1),5,15)
    oled.text("PM10.0= {:2d}".format(reading.pm100_cf1),5,25)
    oled.show()
def main():
    """The main method"""
    # Access the sensor over the serial line.
    sensor = pmsa003.Sensor("0")
    # Reading sensor data until terminated
    while True:
        read_value(sensor)
        #time.sleep(2)
if __name__ == '__main__':
    main()
# EOF

