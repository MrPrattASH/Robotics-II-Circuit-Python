# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#Modified by Brogan Pratt for M4 board
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Audio Out tone example"""
import time
import array
import math
import board
from audioio import AudioOut
from audiocore import RawSample

frequency = 400  # Set this to the Hz of the tone you want to generate.

# Generate one period of sine wav.
length = 8000 // frequency
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int((1 + math.sin(math.pi * 2 * i / length)) * (2 ** 15 - 1))

#init STEMMA Speaker
audio = AudioOut(board.A0)
sine_wave_sample = RawSample(sine_wave)

while True:
    audio.play(sine_wave_sample, loop=True)
    time.sleep(1)
    audio.stop()
    time.sleep(1)
