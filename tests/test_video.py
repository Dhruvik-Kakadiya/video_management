from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Video Management API"}


def test_upload_video():
    video_file = {"file": open("test_video.mp4", "rb")}
    response = client.post("/videos/upload", files=video_file)
    assert response.status_code == 200


def test_search_video():
    response = client.get("/videos/search?name=test")
    assert response.status_code == 200


def test_block_video():
    video_id = 1
    response = client.post(f"/videos/block/{video_id}")
    assert response.status_code == 200


def test_download_video():
    video_id = 1
    response = client.get(f"/videos/download/{video_id}")
    assert response.status_code == 200 or response.status_code == 404
