import os

class ImageCleaner(object):
    def delete_local_image(self, image_path: str):
        if os.path.exists(image_path):
            os.remove(image_path)
            print('{} removed.', image_path)
