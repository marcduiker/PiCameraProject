import os
import time
import picamera
from camerasettings import CameraSettings

STABILIZATION_TIME = 5

class ImageRecorder(object):
    """ Class which controls the image recording of the Pi camera module. """
    def __init__(self, camerasettings, image_base_path):
        self.__camerasettings = camerasettings
        self.__image_base_path = image_base_path

    def capture_image(self):
        """ Method to capture an image using the CameraSettings class. """

        with picamera.PiCamera() as camera:
            camera.resolution = (1640, 1232)
            if not self.__camerasettings.isautomatic:
                camera.awb_mode = self.__camerasettings.whitebalance
                camera.iso = self.__camerasettings.iso
                camera.framerate = self.__camerasettings.framerate
                camera.shutter_speed = self.__camerasettings.shutterspeed
            time.sleep(STABILIZATION_TIME)
            filename = '{}.jpg'.format(time.strftime("%Y%m%d-%H%M%S"))
            filepath = os.path.join(self.__image_base_path, filename)

            print('Starting capture for {}'.format(filename))
            # Pi quality 10 is equal to regular jpeg quality 75. 
            camera.capture(filepath, format='jpeg', resize=(800, 600), quality=11, thumbnail=None)

            return filepath
