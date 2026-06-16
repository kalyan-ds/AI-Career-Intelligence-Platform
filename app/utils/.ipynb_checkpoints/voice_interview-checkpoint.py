import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["PATH"] += os.pathsep + r"C:\Program Files\ffmpeg-8.1.1-essentials_build\bin"


import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import shutil

print(
    shutil.which("ffmpeg")
)

model = whisper.load_model(
    "base"
)

def record_answer():

    duration = 10

    sample_rate = 44100

    recording = sd.rec(

        int(
            duration * sample_rate
        ),

        samplerate=sample_rate,

        channels=1,

        dtype="int16"

    )

    sd.wait()

    audio_file = "temp_answer.wav"

    write(
        audio_file,
        sample_rate,
        recording
    )

    result = model.transcribe(
        audio_file
    )

    return result["text"]

