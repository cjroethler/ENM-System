#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import pantilthat

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
camera = PiCamera()
camera.rotation = 180

def callback(channel):
        if GPIO.input(channel):
                print ("Sound Detected!")
                camera.start_preview(fullscreen=False, window = (1250,10,640,480))
                filename = "/home/pi/Desktop/" + (time.strftime("%y%b%d_%H:%M:%S")) + ".jpg"
                camera.capture(filename)
                #camera.start_preview(fullscreen=False, window = (1250,10,640,480))
                #filename = "/home/pi/Desktop/" + (time.strftime("%y%b%d_%H:%M:%S")) + ".h264"
                #camera.start_recording(filename)
                n = 0
                while n < 100
                    t = time.time()
     
                    # Generate an angle using a sine wave (-1 to 1) multiplied by 90 (-90 to 90)
                    a = math.sin(t * 2) * 90
                   
                    # Cast a to int for v0.0.2
                    a = int(a)
                    
                    # These functions require a number between 90 and -90, then it will snap either the pan or tilt servo to that number in degrees 
                    pantilthat.pan(a)
                    pantilthat.tilt(a)
                 
                    # Two decimal places is quite enough!
                    print(round(a,2))
                 
                    # Sleep for a bit so we're not hammering the HAT with updates
                    time.sleep(0.005)
                    n += 1
        else:
                print ("Sound Detected!")
                camera.start_preview(fullscreen=False, window = (1250,10,640,480))
                filename = "/home/pi/Desktop/" + (time.strftime("%y%b%d_%H:%M:%S")) + ".jpg"
                camera.capture(filename)
                #camera.start_preview(fullscreen=False, window = (1250,10,640,480))
                #filename = "/home/pi/Desktop/" + (time.strftime("%y%b%d_%H:%M:%S")) + ".h264"
                #camera.start_recording(filename)
                   n = 0
                while n < 100
                    t = time.time()
     
                    # Generate an angle using a sine wave (-1 to 1) multiplied by 90 (-90 to 90)
                    a = math.sin(t * 2) * 90
                   
                    # Cast a to int for v0.0.2
                    a = int(a)
                    
                    # These functions require a number between 90 and -90, then it will snap either the pan or tilt servo to that number in degrees 
                    pantilthat.pan(a)
                    pantilthat.tilt(a)
                 
                    # Two decimal places is quite enough!
                    print(round(a,2))
                 
                    # Sleep for a bit so we're not hammering the HAT with updates
                    time.sleep(0.005)
                    n += 1

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)
