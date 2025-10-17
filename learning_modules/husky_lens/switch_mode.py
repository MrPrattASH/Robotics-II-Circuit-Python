import board
from circuitPyHuskyLib import HuskyLensLibrary

# create our husky lens object via i2c communication
huskylens = HuskyLensLibrary("I2C", SCL=board.SCL, SDA=board.SDA)

# verify that our husky lens is connected
print(huskylens.knock()) # should return string "Knock Recieved" if connected


# ---- switch capture modes ----

# list of all the algorithms available on the husky lens
algorithms = ["ALGORITHM_OBJECT_TRACKING",
"ALGORITHM_FACE_RECOGNITION",
"ALGORITHM_OBJECT_RECOGNITION",
"ALGORITHM_LINE_TRACKING",
"ALGORITHM_COLOR_RECOGNITION",
"ALGORITHM_TAG_RECOGNITION",
"ALGORITHM_OBJECT_CLASSIFICATION"]

# switch to selected algorithm index on our list, 
huskylens.algorithm(algorithms[5]) # switch to tag recognition mode
print("Switched to " + algorithms[5])

# this may return "Read response error, please try again"
# as long as tag recognition is displaying on the husky lens screen, you're good. 
