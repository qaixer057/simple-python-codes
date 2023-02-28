# from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.editor as mp

# load the video
video = mp.VideoFileClip(
    "https://staging3.sdsol.com/EquipEducation/Content/Uploads/Attachments/LessonAttachment/videoplayback(1).mp4"
)

# extract the audio
audio = video.audio

# save the audio as mp3 file
audio.write_audiofile("temp_audio.mp3")
