from typing import Optional

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.services.video_service import (
    upload_video,
    search_videos,
    block_video,
    download_video,
)
from app.database import SessionLocal
from app.schemas import VideoResponse

router = APIRouter(prefix="/videos", tags=["Videos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload", response_model=VideoResponse)
async def upload_video_endpoint(
    file: UploadFile = File(...), db: Session = Depends(get_db)
):
    return await upload_video(file, db)


@router.get("/search", response_model=list[VideoResponse])
def search_videos_endpoint(
    name: Optional[str] = None,
    size: Optional[float] = None,
    db: Session = Depends(get_db),
):
    return search_videos(name=name, size=size, db=db)


@router.post("/block/{video_id}")
def block_video_endpoint(video_id: int, db: Session = Depends(get_db)):
    block_video(video_id)
    return {"message": f"Video {video_id} has been blocked"}


@router.get("/download/{video_id}")
def download_video_endpoint(video_id: int, db: Session = Depends(get_db)):
    file_path = download_video(video_id, db)
    if not file_path:
        raise HTTPException(status_code=404, detail="Video not found or is blocked.")
    return FileResponse(
        path=file_path, media_type="video/mp4", filename=file_path.split("/")[-1]
    )
