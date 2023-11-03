import board
import adafruit_am2320
import time

i2c = board.I2C()

sensor = adafruit_am2320.AM2320(i2c)


while True:
    sensor_temp = sensor.temperature
    sensor_humidity = sensor.relative_humidity
    print(f"Temperature: {sensor_temp}")
    print(f"Relative Humidity: {sensor_humidity}")
    time.sleep(2)