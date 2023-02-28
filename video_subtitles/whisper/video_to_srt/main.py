import os
import whisper
from whisper.tokenizer import LANGUAGES, TO_LANGUAGE_CODE
import warnings
import sys
import time
from utils import slugify, write_srt, write_vtt, break_line
import moviepy
import librosa
import moviepy.editor as mp
import numpy as np
import soundfile as sf
from scipy.io import wavfile

model_name = "base"
model = whisper.load_model(model_name)


def video_to_audio(video_path: str):
    video = mp.VideoFileClip(video_path)
    audio = video.audio.write_audiofile("temp_audio.wav")
    temp_file = "temp_audio.wav"
    data = wavfile.read(temp_file)
    input_audio, _ = librosa.load(temp_file, sr=16000)
    os.remove(temp_file)
    return input_audio


def audio_to_srt(video_path: str, save_format="srt"):
    audio = video_to_audio(video_path)
    result = model.transcribe(audio)
    output_dir = os.getcwd()

    if save_format == "srt":
        srt_name = video_path[:-4]
        srt_path = os.path.join(output_dir, f"{slugify(srt_name)}.srt")
        with open(srt_path, "w", encoding="utf-8") as srt:
            write_srt(result["segments"], file=srt)
            srt.close()
        print(f"Srt-File saved to {srt_path}")
    elif save_format == "vtt":
        vtt_name = video_path[:-4]
        vtt_path = os.path.join(output_dir, f"{slugify(vtt_name)}.vtt")
        with open(vtt_path, "w", encoding="utf-8") as vtt:
            write_vtt(result["segments"], file=vtt)
            vtt.close()
        print(f"VTT-File saved to {vtt_path}")
    else:
        print("Please enter a subtitle format rule.")


if __name__ == "__main__":
    try:
        t1 = time.time()
        audio_to_srt("video.mp4", save_format="vtt")
        t2 = time.time()
        print(f"file generation took {t2-t1} seconds")
    except KeyboardInterrupt:
        pass
    sys.exit()
