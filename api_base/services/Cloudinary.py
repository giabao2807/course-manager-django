import os

import cloudinary
import cloudinary.uploader


class CloudinaryService:

    @classmethod
    def upload_avatar(cls, image):
        return cloudinary.uploader.upload(image, folder='/boni/')