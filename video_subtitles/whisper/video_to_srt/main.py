import os
import whisper
from whisper.tokenizer import LANGUAGES, TO_LANGUAGE_CODE
import warnings

# import yt_dlp
from utils import slugify, write_srt, write_vtt, break_line

# import tempfile

import moviepy
import librosa
import moviepy.editor as mp
import numpy as np
import soundfile as sf
from scipy.io import wavfile

model_name = "base"
model = whisper.load_model(model_name)


def video_to_audio(video_path):
    video = mp.VideoFileClip(video_path)
    audio = video.audio.write_audiofile("temp_audio.wav")
    temp_file = "temp_audio.wav"
    data = wavfile.read(temp_file)
    input_audio, _ = librosa.load(temp_file, sr=16000)
    os.remove(temp_file)
    return input_audio


def audio_to_srt(video_path, save_format="srt"):
    audio = video_to_audio(video_path)
    result = model.transcribe(audio)
    # srt_path = os.getcwd()
    output_dir = os.getcwd()
    srt_name = video_path[:-4]
    srt_path = os.path.join(output_dir, f"{slugify(srt_name)}.srt")
    if save_format == "srt":
        with open(srt_path, "w", encoding="utf-8") as srt:
            write_srt(result["segments"], file=srt)
            srt.close()
    print(f"file saved to {srt_path}")


audio_to_srt("video.mp4")
