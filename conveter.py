import librosa
import numpy as np
from scipy.io import wavfile

import librosa
import soundfile as sf

# Load an audio file. Replace 'original_audio_file.wav' with your audio file path.
y, sr = librosa.load('./samples/powerset.wav', sr=None)

# Define the target sample rate. For example, to resample to 16000 Hz.
target_sr = 16000

# Perform the resampling
y_resampled = librosa.resample(y, orig_sr = sr, target_sr = target_sr)

# Save the resampled audio to a new file. Replace 'resampled_audio_file.wav' with your desired output file name.
sf.write('./samples/powerset.wav', y_resampled, target_sr)
