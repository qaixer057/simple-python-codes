import moviepy.editor as mp
import speech_recognition as sr
import pysrt

video = mp.VideoFileClip("video.mp4")

audio = video.audio.write_audiofile("temp_audio.wav", bitrate="32k")
print(type(audio))

recognizer = sr.Recognizer()
with sr.AudioFile("temp_audio.wav") as source:
    audio_data = recognizer.record(source)
    print("Recognizing audio data...")
    transcript = recognizer.recognize_bing(audio_data, language="en-US")

print("writing to external srt file...")
srt_file = pysrt.SubRipFile()
srt_file.append(
    pysrt.SubRipItem(
        index=1,
        text=transcript,
        start=pysrt.SubRipTime(0, 0, 0),
        end=pysrt.SubRipTime(hours=0, minutes=0, seconds=4),
    )
)
srt_file.save("video.srt", encoding="utf-8")
