import moviepy.editor as mp
import pysrt

# Load video file
video = mp.VideoFileClip("video.mp4")

# Open the SRT file
srt_file = pysrt.open("video.srt")

# Iterate through each subtitle and adjust the times
for i, subtitle in enumerate(srt_file):
    start_time = subtitle.start.to_time()
    end_time = subtitle.end.to_time()

    # Adjust the times based on the duration of the video
    start_time += video.start
    end_time += video.start

    subtitle.set_start_time(start_time)
    subtitle.set_end_time(end_time)

    # Update the index of the subtitle
    subtitle.index = i + 1

# Save the updated SRT file
srt_file.save("video_synced.srt", encoding="utf-8")
