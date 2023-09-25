#
# Based on:
# https://gitlab.cba.mit.edu/neilg/urumbu/-/blob/master/serialstep/serialstep.1.py 
#
# This program connects to a stepper motor Urumbu module and controls it.
# The motor will continuously rotate 1 full revolution clockwise and then back again 

import serial,sys,time,signal

if (len(sys.argv) != 4):                                       # If the incorrect number of arguments is given
   print("command line: serialstep.1.py port speed delay")     # Print a help message to the terminal
   sys.exit()                                                  # and exit the program
   
device = sys.argv[1]                                           # Argument 1 is the port of the device (e.g. '/dev/ttyUSB0')
baud = int(sys.argv[2])                                        # Argument 2 is the baud rate of the device (e.g. '9600')
delay = float(sys.argv[3])                                     # Argument 3 is the delay between steps in seconds (e.g. '0.001')

print('open '+device+' at '+str(baud)+' delay '+str(delay))    # Print to the console to show the user request
port = serial.Serial(device,baudrate=baud,timeout=0)           # connect to the serial port

print('Serial Port Opened')

#---------------------------------------------------------------------------------------------------------------------------------

count = 0                                                      # total number of steps
stepsPerRevolution = 1600                                      # total number of steps per revolution
forward = b'f'                                                 # send 'f' to drive the motor forward/clockwise
reverse = b'r'                                                 # send 'r' to drive the motor reverse/anti-clockwise

#---------------------------------------------------------------------------------------------------------------------------------
while(1):                                                      # loop until the program is terminated
    
   while (count < stepsPerRevolution):                         # loop until a full clockwise revolution has been completed
      port.write(forward)                                      # send an 'f' to the Urumbu device to rotate 1 step clockwise        
      print("Forward")
      count += 1                                               # add 1 to the step count
      time.sleep(delay)                                        # wait the specified time (in seconds)
      
   while (count < stepsPerRevolution*2):                       # loop until a full anti-clockwise revolution has been completed
      port.write(reverse)                                      # send an 'r' to the Urumbu device to rotate 1 step anti-clockwise
      print("Reverse")
      count += 1                                               # add 1 to the step count
      time.sleep(delay)                                        # wait the specified time (in seconds)
      
   count = 0                                                   # reset the step count before looping