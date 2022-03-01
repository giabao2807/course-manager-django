from api_base.services import CloudinaryService


class StudentService:

    @classmethod
    def upload_avatar(cls, image):
        res_data = CloudinaryService.upload_avatar(image)
        return res_data.get("url")