from minio import Minio
from app.config import settings
import uuid

minio_client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=settings.MINIO_USE_SSL

def upload_image_to_minio(file_obj, content_type):
    filename = f"{uuid.uuid4()}.jpg"
    minio_client.put_object(
        settings.MINIO_BUCKET,
        filename,
        file_obj,
        length=-1,
        part_size=10 * 1024 * 1024,
        content_type=content_type
    )
    return f"{settings.MINIO_BASE_URL}/{settings.MINIO_BUCKET}/{filename}"
