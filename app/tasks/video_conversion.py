import os


async def convert_to_mp4(video_path: str):
    mp4_path = video_path.rsplit(".", 1)[0] + ".mp4"

    # Simulate video conversion logic here
    # Use libraries like moviepy or ffmpeg-python for real conversion
    os.rename(video_path, mp4_path)  # Fake conversion (just renaming in this case)

    return mp4_path
