import pulseio
import board
import time
import array

#command every 20ms
pulses = pulseio.PulseIn(board.D0, maxlen=100, idle_state=False)
on_command = array.array('H',[pulses[x] for x in range(len(pulses))])
while True:
    if len(pulses) >0:
        print(pulses[0])
    time.sleep(.1)# Write your code here :-)
