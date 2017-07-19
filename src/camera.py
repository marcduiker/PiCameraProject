import os
import time
import picamera
from camerasettings import CameraSettings

picturePath = '/home/msd/Pictures/PiCam/'

def captureimage(settings):
    
    sleeptime = 8

    with picamera.PiCamera() as camera:
        camera.resolution = (1640, 1232)
        camera.quality = 80
        if settings.isautomatic == False:
            camera.awb_mode = settings.whitebalance
            camera.iso = settings.iso
            camera.framerate = settings.framerate
            camera.shutter_speed = settings.shutterspeed
        time.sleep(sleeptime)
        filename = '{}.jpg'.format(time.strftime("%Y%m%d-%H%M%S"))
        filepath = os.path.join(picturePath, filename)
        camera.capture(filepath)


camsettings = CameraSettings()
#settings.iso = 1600
#settings.whitebalance = 'auto'
#settings.shutterspeed = 4
#settings.framerate = 6
captureimage(camsettings)
