import time
import datetime
from imagerecorder import ImageRecorder
from camerasettings import CameraSettings
from imageuploader import ImageUploader
from imagecleaner import ImageCleaner

image_base_path = '/home/msd/Pictures/PiCam/'
total_frames = 5
current_frame = 1
sleep_time = 5
while current_frame < total_frames:
    camera_settings = CameraSettings()
    start_morning_hour = 6
    start_evening_hour = 22
    current_hour = datetime.datetime.now().hour 
    if current_hour >= start_evening_hour or current_hour <= start_evening_hour:
        # longer exposure and higher ISO for the night
        camera_settings.isautomatic = False
        camera_settings.exposuremode = 'off'
        camera_settings.framerate = 6
        camera_settings.iso = 800
        camera_settings.shutterspeed = 4 # seconds

    image_path = ImageRecorder(camera_settings, image_base_path).capture_image()
    ImageUploader().store_image(image_path)
    ImageCleaner().delete_local_image(image_path)
    
    time.sleep(sleep_time)
    current_frame += 1