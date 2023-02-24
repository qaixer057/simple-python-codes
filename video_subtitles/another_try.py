import moviepy.editor as mp
import pysrt
import datetime

# Load video file
video = mp.VideoFileClip("video.mp4")

# Open the SRT file
srt_file = pysrt.open("video.srt")

# Iterate through each subtitle and adjust the times
for i, subtitle in enumerate(srt_file):
    start_time = subtitle.start.to_time()
    end_time = subtitle.end.to_time()

    # Convert the time to a datetime object and add the video start time
    start_datetime = datetime.datetime.combine(
        datetime.date.today(), start_time
    ) + datetime.timedelta(seconds=video.start)
    end_datetime = datetime.datetime.combine(
        datetime.date.today(), end_time
    ) + datetime.timedelta(seconds=video.start)

    # Convert the datetime objects back to time objects
    start_time = start_datetime.time()
    end_time = end_datetime.time()

    subtitle.set_start_time(start_time)
    subtitle.set_end_time(end_time)

    # Update the index of the subtitle
    subtitle.index = i + 1

# Save the updated SRT file
srt_file.save("video_synced.srt", encoding="utf-8")
