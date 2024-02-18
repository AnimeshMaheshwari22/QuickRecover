import pyaudio
import numpy as np
import wave

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
GAP_THRESHOLD = RATE // CHUNK * RECORD_SECONDS  # Number of chunks for 5-second gap

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                     rate=RATE, input=True,
                     frames_per_buffer=CHUNK)

# Variable to keep track of gap time
gap_time = 0

# Variable to keep track of file number
file_number = 1

# List to store audio data during gap
frames = []

# Start recording
print("Recording...")

try:
    while True:
        data = stream.read(CHUNK)
        audio_data = np.frombuffer(data, dtype=np.int16)
        
        # Check if there is a gap
        if np.max(audio_data) < 100:
            gap_time += 1
            frames.append(data)
            if gap_time >= GAP_THRESHOLD:
                print(f"Gap detected. Saving audio file {file_number}")
                gap_time = 0
                file_name = f"audio_{file_number}.wav"
                wf = wave.open(file_name, 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(audio.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                wf.close()
                frames = []  # Reset frames list for next file
                file_number += 1
        else:
            gap_time = 0
            frames.append(data)

except KeyboardInterrupt:
    pass

# Close stream
stream.stop_stream()
stream.close()
audio.terminate()
