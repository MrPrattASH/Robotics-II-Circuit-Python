# Mono Analog Audio Out

This tutorial will teach you how to use the STEMMA mono audio amplifier/Speaker. **Original tutorial taken from [here at adafruit](https://learn.adafruit.com/circuitpython-essentials/circuitpython-audio-out) and it has been modified to suit the M4 board without button use.** 

The first example will show you how to generate a tone and play it using a button. The second example will show you how to play, pause, and resume a wave file using a button to resume. Both will play the audio through the STEMMA Speaker. You can change the volume via the turning dial on the STEMMA speaker with a phillips head screwdriver. 

In our code, we'll use pin A0 for our audio output, though you can also output true analog to A1.

## Play a Tone
Copy and paste the following code from play_tone.py above into code.py using Mu, and save the file.

### Code explanation
If the volume is too high, reduce the turn dial on the STEMMA speaker with a small phillips driver. 
To set the frequency of the generated tone, change the number assigned to the frequency variable to the Hz of the tone you'd like to generate.

First, we generate one period of a sine wave with the math.sin function, and assign it to sine_wave.
Next, we create the audio object (the STEMMA Speaker), and assign it to pin A1.
We create a sample of the sine wave by using RawSample and providing the sine_wave we created.

In the Loop, we play the sample we created and we loop it. The time.sleep(1) tells it to loop (play) for 1 second. Then we stop it after 1 second is up. You can increase or decrease the length of time it plays by increasing or decreasing the number of seconds provided to time.sleep(). Try changing it from 1 to 0.5. Now try changing it to 2. You can change it to whatever works for you!

That's it!

## Play a WAV File
You can use any supported wave file you like. CircuitPython supports mono or stereo, at 22 KHz sample rate (or less) and 16-bit WAV format. The STEMMA Speaker supports ONLY MONO. (unless of course, you hook up 2 STEMMA speakers to A0 and A1 respectively) The M4 boards support stereo as they have two outputs. The 22 KHz or less because the circuitpython can't handle more data than that (and also it will not sound much better) and the DAC output is 10-bit so anything over 16-bit will just take up room without better quality.

Since the WAV file must fit on the CircuitPython file system, **it must be under 2 MB.** CircuitPython does not support OGG. Just WAV and MP3!
We have a detailed guide on how to generate WAV files [here](https://learn.adafruit.com/adafruit-wave-shield-audio-shield-for-arduino/check-your-files)

We've included the one we used here. Download it from the files above (Street Chicken) and copy it to the main directory of your board. (not inside lib, the main CIRCUITPY drive)
We're going to loop the wave file for 6 seconds. 

Copy and paste the following code "play_wav.py" into code.py using your favorite editor, and save the file.

### Code Explanation
First we then open the file, "StreetChicken.wav" as a readable binary and store the file object in wave_file which is what we use to actually read audio from: wave_file = open("StreetChicken.wav", "rb").

Now we will ask the audio playback system to load the wave data from the file wave = audiocore.WaveFile(wave_file) and finally request that the audio is played through the A0 analog output pin audio = audioio.AudioOut(board.A1).

The audio file is now ready to go, and can be played at any time with audio.play(wave)!

Inside our loop, we start by playing the file.

Next we have the block that tells the code to wait 6 seconds before pausing the file. We chose to go with using time.monotonic() because it's **non-blocking** which means you can do other things while the file is playing, like control servos or NeoPixels! At any given point in time, time.monotonic() is equal to the number seconds since your board was last power-cycled. (The soft-reboot that occurs with the auto-reload when you save changes to your CircuitPython code, or enter and exit the REPL, does not start it over.) When it is called, it returns a number with a decimal. When you assign time.monotonic() to a variable, that variable is equal to the number of seconds that time.monotonic() was equal to at the moment the variable was assigned. You can then call it again and subtract the variable from time.monotonic() to get the amount of time that has passed. For more details, check out this example.

So, we assign t = time.monotonic() to get a starting point. Then we say pass, or "do nothing" until the difference between t and time.monotonic() is greater than 6seconds. In other words, continue playing until 6 seconds passes. Remember, you can add in other code here to do other things while you're playing audio for 6 seconds.

Finally, we print to the serial console, "Done!"

You can do this with any supported wave file, and you can include all kinds of things in your project while the file is playing. Give it a try!


