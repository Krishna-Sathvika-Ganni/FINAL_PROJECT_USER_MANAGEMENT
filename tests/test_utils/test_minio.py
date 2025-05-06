import io
from unittest.mock import patch
from app.utils.minio import upload_image_to_minio,get_image_url_from_minio
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

def test_get_image_url_from_minio():
    file_name = "example.jpg"
    url = get_image_url_from_minio(file_name)

    assert file_name in url
    assert url.startswith("http") or url.startswith("https")

@patch("app.utils.minio.uuid.uuid4")
@patch("app.utils.minio.minio_client.put_object")
def test_unicode_filename(mock_put_object, mock_uuid):
    mock_uuid.return_value = "test-unicode-uuid"
    dummy_file = io.BytesIO(b"dummy image data")
    content_type = "image/jpeg"
    filename = "unicode_テスト_🌟.jpg"
    
    url = upload_image_to_minio(dummy_file, content_type, filename)
    
    mock_put_object.assert_called_once()
    assert "test-unicode-uuid.jpg" in url
    assert "テスト" not in url
    assert "🌟" not in url

