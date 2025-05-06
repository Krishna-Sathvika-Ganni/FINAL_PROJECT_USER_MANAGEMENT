import io
from unittest.mock import patch
from app.utils.minio import upload_image_to_minio

@patch("app.utils.minio.minio_client.put_object")
def test_upload_image_to_minio(mock_put_object):
    dummy_file = io.BytesIO(b"dummy image data")
    dummy_file.seek(0)
    content_type = "image/jpeg"
    filename = "test.jpg"

    url = upload_image_to_minio(dummy_file, content_type, filename)

    assert url.endswith(".jpg")
    mock_put_object.assert_called_once()
