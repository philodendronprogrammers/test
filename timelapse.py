from picamera import PiCamera
from os import system
import os
from time import sleep

os.chdir('/home/pi/mnt/gdrive/plantpics')
camera = PiCamera()
camera.resolution = (1024, 768)

for i in range(10):
    camera.capture('image{0:04d}.jpg'.format(i))
    sleep(10800)
    print("captured")
            
system('convert -delay 10 -loop 0 image*.jpg animation.gif')

camera.close()
