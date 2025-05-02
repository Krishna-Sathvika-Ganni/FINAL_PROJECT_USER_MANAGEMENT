from minio import Minio
from settings.config import settings
import uuid

minio_client = Minio(
    settings.minio_endpoint,
    access_key=settings.minio_access_key,
    secret_key=settings.minio_secret_key,
    secure=settings.minio_use_ssl
)

def upload_image_to_minio(file_obj, content_type, filename):
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{ext}"
    minio_client.put_object(
        settings.minio_bucket_name,
        unique_filename,
        file_obj,
        length=-1,
        part_size=10 * 1024 * 1024,
        content_type=content_type
    )
    return f"{settings.minio_base_url}/{settings.minio_bucket_name}/{unique_filename}"

def get_image_url_from_minio(file_name: str) -> str:
    return f"{settings.minio_base_url}/{settings.minio_bucket_name}/{file_name}"
