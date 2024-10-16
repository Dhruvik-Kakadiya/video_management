import os
from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException
from app.models import Video
from app.schemas import VideoResponse
from app.tasks.video_conversion import convert_to_mp4
from app.utils.cache import is_blocked, block_video_in_cache

UPLOAD_DIR = "uploads/"


async def upload_video(file: UploadFile, db: Session):
    # Ensure the upload directory exists
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    if not file.filename.endswith(("mp4", "mkv", "avi")):
        raise HTTPException(status_code=400, detail="Invalid video format")

    # Save the uploaded video
    video_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(video_path, "wb") as f:
        f.write(await file.read())

    # Convert video asynchronously
    mp4_path = await convert_to_mp4(video_path)

    # Add to database
    video = Video(
        name=file.filename, path=mp4_path, size=os.path.getsize(mp4_path), format="mp4"
    )
    db.add(video)
    db.commit()
    db.refresh(video)

    return VideoResponse.from_orm(video)


def search_videos(name: str = None, size: float = None, db: Session = None):
    query = db.query(Video)
    if name:
        query = query.filter(Video.name.contains(name))
    if size:
        query = query.filter(Video.size == size)
    return query.all()


def block_video(video_id: int):
    # Block the video by adding its ID to Redis cache
    block_video_in_cache(video_id)


def download_video(video_id: int, db: Session):
    if is_blocked(video_id):
        return None  # Video is blocked

    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        return None  # Video not found

    return video.path
