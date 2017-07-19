import os
from azureconfig import AZURE_STORAGE as storageconfig
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

def upload_callback(current, total):
    if current == total:
        print("Upload finished.")

class ImageUploader(object):

    def store_image(self, image_path: str, subcontainer: str = None):
        """ Saves the image to Azure Blob storage in an optional subcontainer. """
        block_blob_service = BlockBlobService(
            account_name=storageconfig['accountname'],
            account_key=storageconfig['accountkey'])

        image_name = os.path.basename(image_path)
        if subcontainer != None:
            blob_name = '/'.join((subcontainer, image_name))
        else:
            blob_name = image_name
        
        print('Starting image upload to Azure for {}'.format(image_path))
        
        block_blob_service.create_blob_from_path(
            container_name=storageconfig['container'],
            blob_name=blob_name,
            file_path=image_path,
            content_settings=ContentSettings(content_type='image/jpeg'),
            progress_callback=upload_callback
            )