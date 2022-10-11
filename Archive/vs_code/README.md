Install Visual Studio Code first. See relevant repo folder. 

## Opening CircuitPython on VS Code
Follow Steps 3-7 [on this site](https://sites.google.com/view/circuitpython/development-environments/visual-studio-code-setup)

## Pushing code to your MetroM4 Airlift Lite
on VS Code, 
- File > Open Folder > CIRCUITPY (*The actual drive*)
- Select code.py in left side

- CMD+S saves written code, and reboots device
- in VSCode View > Command Pallette (CMD+SHFT+P) > CircuitPython:Open Serial Monitor

## Troubleshooting Serial Monitor in VS Code
If you have disconnected the MetroM4 from your computer, The serial monitor connection will be broken. Sometimes it will re-boot back in, sometimes it will not. Try these steps.

1. Verify that VSCode has the CIRCUITPY drive open. This is what VS Codes' file explorer looks like with a previously connected CIRCUITPY drive, not disconnected. Notice the yellow !
 <img width="112" alt="Screen Shot 2022-06-02 at 09 38 27" src="https://user-images.githubusercontent.com/101632496/171578793-3645ea55-4d46-4b58-8b7e-b1ee624d91bd.png">
If the drive is not connected, often times you can click the refresh button. If not,  File > Open > CIRCUITPY drive (yes, the entire drive)

2. With your drive connected, close the serial monitor (View > Command Pallette > CircuitPython:Close Serial Monitor), then re-open the serial monitor
3. Verify that you are connected to the correct serial port, and have the correct board connected. It should look like this:
<img width="641" alt="Screen Shot 2022-06-02 at 09 42 00" src="https://user-images.githubusercontent.com/101632496/171579767-00a5bd26-56d3-4a39-be30-6a74d30e5517.png">
4. use a simple CTRL+D inside the terminal to reboot your board, you should now see serial output again. 
