from minio import Minio
from settings.config import settings
import uuid

minio_client = Minio(
    settings.minio_endpoint,
    access_key=settings.minio_access_key,
    secret_key=settings.minio_secret_key,
    secure=settings.minio_base_url
)

def upload_image_to_minio(file_obj, content_type):
    filename = f"{uuid.uuid4()}.jpg"
    minio_client.put_object(
        settings.minio_bucket_name,
        filename,
        file_obj,
        length=-1,
        part_size=10 * 1024 * 1024,
        content_type=content_type
    )
    return f"{settings.minio_base_url}/{settings.minio_bucket_name}/{filename}" 
