#
# Based on:
# https://gitlab.cba.mit.edu/neilg/urumbu/-/blob/master/serialstep/serialstep.1.py 
#
# This program connects to a stepper motor Urumbu module and controls it.
# The user can press the left or right arrow keys to rotate the motor clockwise or anticlockwise.

import serial,sys,time,signal,keyboard

if (len(sys.argv) != 3):                                       # If the incorrect number of arguments is given
   print("command line: serialstep.1.py port speed")           # Print a help message to the terminal
   sys.exit()                                                  # and exit the program
   
device = sys.argv[1]                                           # Argument 1 is the port of the device (e.g. '/dev/ttyUSB0')
baud = int(sys.argv[2])                                        # Argument 2 is the baud rate of the device (e.g. '9600')

print('open '+device+' at '+str(baud))                         # Print to the console to show the user request
port = serial.Serial(device,baudrate=baud,timeout=0)           # connect to the serial port

print('Serial Port Opened')

#---------------------------------------------------------------------------------------------------------------------------------

delay = 0.001                            
forward = b'f'                                                 # send 'f' to drive the motor forward/clockwise
reverse = b'r'                                                 # send 'r' to drive the motor reverse/anti-clockwise

#---------------------------------------------------------------------------------------------------------------------------------
while(1):                                                      # loop until the program is terminated
    
    if keyboard.is_pressed('right'):                           # If the right arrow key is pressed
        port.write(forward)                                    # send an 'f' to the Urumbu device to rotate 1 step clockwise
        print("Forward")
        
    if keyboard.is_pressed('left'):                            # If the left arrow key is pressed
        port.write(reverse)                                    # send an 'r' to the Urumbu device to rotate 1 step anti-clockwise
        print("Reverse")
    
    time.sleep(delay)                                          # wait the specified time (in seconds)