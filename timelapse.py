from picamera import PiCamera
from os import system
from time import sleep
import os
import git


camera = PiCamera()
camera.resolution = (1024, 768)
repo = git.Repo("/bin/pictures")



for i in range(10):
    os.chdir('/bin/pictures')
    camera.capture('image{0:04d}.jpg'.format(i))
    #sleep(10800)
    system('convert -delay 5 -loop 0 image*.jpg animation.gif')
    repo.git.add(A=True)
    repo.index.commit("test")
    origin = repo.remote(name='origin')
    origin.push(username='philodendronprogrammers', password='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')

    
    

   
    print("captured 1")

camera.close()



   # os.chdir('/bin/pictures')

            




