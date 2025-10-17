import board
from circuitPyHuskyLib import HuskyLensLibrary

# create our husky lens object via i2c communication
huskylens = HuskyLensLibrary("I2C", SCL=board.SCL, SDA=board.SDA)

# verify that our husky lens is connected
print(huskylens.knock()) # should return string "Knock Recieved" if connected


