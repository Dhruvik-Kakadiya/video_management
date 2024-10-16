from pydantic import BaseModel


class VideoCreate(BaseModel):
    name: str


class VideoResponse(BaseModel):
    id: int
    name: str
    path: str
    size: float
    format: str

    class Config:
        orm_mode = True
        from_attributes = True
