import os
from queue import Queue

class ImageCleaner(object):
    def __init__(self, images_to_delete: Queue):
        self.images_to_delete = images_to_delete

    def delete_local_image(self):
        if not self.images_to_delete.empty():
            image_path = self.images_to_delete.get()
            if os.path.exists(image_path):
                os.remove(image_path)
                print('{} removed.', image_path)
