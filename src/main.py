import time
import datetime
from imagerecorder import ImageRecorder
from camerasettings import CameraSettings
from imageuploader import ImageUploader
from imagecleaner import ImageCleaner

IMAGE_BASE_PATH = '/home/msd/Pictures/PiCam/'
SLEEP_TIME = 5
START_MORNING_HOUR = 5
START_EVENING_HOUR = 23
END_DATE = datetime.datetime(2017, 7, 28, 12, 0, 0)

current_frame = 0

while datetime.datetime.now() < END_DATE:
    camera_settings = CameraSettings()
    current_hour = datetime.datetime.now().hour 
    if current_hour >= START_EVENING_HOUR or current_hour <= START_MORNING_HOUR:
        # longer exposure and higher ISO for the night
        camera_settings.isautomatic = False
        camera_settings.exposuremode = 'off'
        camera_settings.framerate = 6
        camera_settings.iso = 800
        camera_settings.shutterspeed = 4 # seconds

    image_path = ImageRecorder(camera_settings, IMAGE_BASE_PATH).capture_image()
    ImageUploader().store_image(image_path, time.strftime("%Y%m%d"))
    ImageCleaner().delete_local_image(image_path)
    
    time.sleep(SLEEP_TIME)
    current_frame += 1

print("{} images captured.".format(current_frame))