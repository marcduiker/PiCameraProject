import time
import picamera
import os
import fractions

picturePath = '/home/msd/Pictures/PiCam/'

def captureimage(settings):
    
    sleepTime = 8

    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.awb_mode = settings.whitebalance
        camera.iso = settings.iso
        camera.framerate = fractions.Fraction(1, 6)
        camera.shutter_speed = settings.shutterspeed
        time.sleep(sleepTime)
        fileName = '{}.jpg'.format(time.strftime("%Y%m%d-%H%M%S"))
        filePath = os.path.join(picturePath, fileName)
        camera.capture(filePath)

class CameraSettings:
    def _init(self):
        # defaults
        self._iso = 400
        self._whitebalance = 'auto'
        self._shutterspeed = None

    @property
    def iso(self):
        return self._iso
    
    @iso.setter
    def iso(self, value):
        self._iso = value

    @property
    def whitebalance(self):
        return self._whitebalance
    
    @whitebalance.setter
    def whitebalance(self, value):
        self._whitebalance = value

    @property
    def shutterspeed(self):
        return self._shutterspeed
    
    @shutterspeed.setter
    def shutterspeed(self, value):
        self._shutterspeed = value * 1000000


settings = CameraSettings()
settings.iso = 1600
settings.whitebalance = 'auto'
settings.shutterspeed = 4
captureimage(settings)
