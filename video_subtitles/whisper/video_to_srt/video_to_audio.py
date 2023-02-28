import requests
from io import BytesIO
from pydub import AudioSegment

video_url = "https://staging3.sdsol.com/EquipEducation/Content/Uploads/Attachments/LessonAttachment/videoplayback(1).mp4"

# Send a GET request to the video URL and read the content into memory
response = requests.get(video_url)
video_content = response.content

# Use BytesIO to create a stream of the video content
video_stream = BytesIO(video_content)

# Load the video into pydub's AudioSegment
video_audio = AudioSegment.from_file(video_stream, format="mp4")

# Export the audio as a .mp3 file
audio_file = "video_audio.mp3"
video_audio.export(audio_file, format="mp3")
