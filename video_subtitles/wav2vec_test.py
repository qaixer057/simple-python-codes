import torch
import moviepy.editor as mp
import librosa
import numpy as np
import soundfile as sf
from scipy.io import wavfile
import pysrt

# from IPython.display import Audio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

video = mp.VideoFileClip("video.mp4")
audio = video.audio.write_audiofile("temp_audio.wav")

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

temp_file = "temp_audio.wav"

data = wavfile.read(temp_file)
framerate = data[0]
sounddata = data[1]
time = np.arange(0, len(sounddata)) / framerate
print("Sampling rate:", framerate, "Hz")

input_audio, _ = librosa.load(temp_file, sr=16000)

input_values = tokenizer(input_audio, return_tensors="pt").input_values
logits = model(input_values).logits
predicted_ids = torch.argmax(logits, dim=-1)
transcription = tokenizer.batch_decode(predicted_ids)[0]
del temp_file
print(transcription)

print("writing to external srt file...")
srt_file = pysrt.SubRipFile()
srt_file.append(
    pysrt.SubRipItem(
        index=1,
        text=transcription,
        start=pysrt.SubRipTime(0, 0, 0),
        end=pysrt.SubRipTime(hours=0, minutes=0, seconds=59),
    )
)
srt_file.save("video.srt", encoding="utf-8")

"""
# need to try Whisper, Vosk, and Nvidia NeMO
import whisper

model = whisper.load_model("base")
result = model.transcribe("opto_sessions_ep_69_excerpt.wav")
print(result["text"])
"""
