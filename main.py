import adafruit_veml7700
import adafruit_mcp9808
import adafruit_am2320
import adafruit_adt7410
import board
import busio

#i2c_veml = busio.I2C(board.SCL, board.SDA)
i2c = board.I2C()

#i2c = board.STEMMA_I2C()


veml7700 = adafruit_veml7700.VEML7700(i2c_veml)

adt = adafruit_adt7410.ADT7410(i2c, address=0x48)
adt.high_resolution = True

mcp = adafruit_mcp9808.MCP9808(i2c)

#sensor = adafruit_am2320.AM2320(i2c)


print(f"Ambient light: {veml7700.light}")
print(f"Lux: {veml7700.lux}")
print('\n')

print(f"ADT Temp: {adt.temperature}")
print('\n')

print(f"MCP Temp: {mcp.temperature}")
print('\n')

#print(f"AM2320 Temp: {sensor.temperature}")
#print(f"AM2320 Humidity: {sensor.relative_humidity}")