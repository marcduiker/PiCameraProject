import time
from imagerecorder import ImageRecorder
from camerasettings import CameraSettings
from imageuploader import ImageUploader
from imagecleaner import ImageCleaner

image_base_path = '/home/msd/Pictures/PiCam/'
total_frames = 5
current_frame = 1
while current_frame < total_frames:
    camera_settings = CameraSettings()
    # Change default camera settings here if required
    image_path = ImageRecorder(camera_settings, image_base_path).capture_image()
    ImageUploader().store_image(image_path)
    ImageCleaner().delete_local_image(image_path)
    time.sleep(5)