import board
import adafruit_am2320
import time

i2c = board.I2C()

sensor = adafruit_am2320.AM2320(i2c)

while True:
    print(f"Temperature: {sensor.temperature}")
    print(f"Relative Humidity: {sensor.relative_humidity}")
    time.sleep(2)