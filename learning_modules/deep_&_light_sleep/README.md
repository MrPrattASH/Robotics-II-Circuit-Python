# Deep & Light Sleep Circuit Python Tutorial

Sometimes we make power hungry projects. CircuitPython boards have a function called "deep" or "light" sleep to reduce power draw. This can be especially useful in "permanent" installed machines like weather stations or plant watering devices. We might want to use deep or light sleep to reduce power consumption and extend battery life. Deep sleep reduces power consumption to the minimum by shutting down everything except for the real-time clock (RTC) and some low-power RAM. Light sleep keeps sufficient state so the program can resume after sleeping. It does not shut down WiFi, BLE, or other communications, or ongoing activities such as audio playback. It reduces power consumption to the extent possible that leaves these continuing activities running.

* Light sleep keeps sufficient state so the program can resume after sleeping. It does not shut down WiFi, BLE, or other communications, or ongoing activities such as audio playback. In practice, this isn't a ton. 
* Deep sleep reduces power consumption to the minimum by shutting down everything except for the real-time clock (RTC) and some low-power RAM. Once the program "awakes" it starts the program from the beginning again. 
* in most sleep programs, we **do not have a while true loop**

## Power Reductions on Metro M4 Airlift Lite
* When running a while true loop: 33mA
* Idle (finished program running): 16.5mA
* In deep sleep mode: 7.4mA 
* In light sleep mode: 15.5mA

## Installing Relevant Libraries

Before beginning, you will need the relevant libraries that will do a lot of the heavy lifting for us. Install these to your M4 lib folder They are located in the folders/files above. Be sure to download the entire folder contents for the bottom 2, not just the .mpy files. (unsure how to download files from GitHub? See [these instructions](https://www.itprotoday.com/development-techniques-and-management/how-do-i-download-files-github)):
* alarm

## Example Code
Located in the folder above:
* deep_sleep_example.py
* light_sleep_example.py
* button_high_pin_alarm_example.py
* multiple_repeating_alarms_example.py

Read through code comments to understand the code, then, copy/paste this code into your metro m4 board and watch the serial output.
Notes:
* while the board is plugged into your computer, it will provide a "fake" sleep, and will not actually reduce power consumption
* after watching the serial output, plug your m4 into an external power supply and watch the LED output for the program. 
