# Saving & Loading Trained Models
It is possible to train machine learning models on one husky lens, save this data onto a microSD card, then transfer this data over to another husky lens. 

*Be cautious with microSD cards, they can be rather delicate. Ensure you are inserting and removing them straight*

## SD card location 

The microsd card slot is on the front face of the husky lens

![photo](images/sd_card.png)

## Saving Models Code

After training a model on the husky lens, you can save the model as any 4 digit integer. I suggest you use your birth date, birth month. For example:
* Jan 10 would be `1001`
* May 15 would be `1505`

```python
import board
import time
from circuitPyHuskyLib import HuskyLensLibrary

hl = HuskyLensLibrary('I2C', SDA=board.SDA, SCL=board.SCL)
hl.algorithm("ALGORITHM_FACE_RECOGNITION") # Redirect to Face Recognition Function

hl.saveModelToSDCard(9999)
time.sleep(2) # add a 2 second sleep to give the Husky Lens time to respond

```