import pyaudio
import struct
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wav
from scipy.fftpack import fft

mic = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 50000
CHUNK = int(RATE/20)
stream = mic.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK)

fig, ax = plt.subplots(figsize=(14,6))
x = np.arange(0, 2 * CHUNK, 2)
ax.set_ylim(-20000, 20000)
ax.set_xlim(0, CHUNK) #make sure our x axis matched our chunk size
line, = ax.plot(x, np.random.rand(CHUNK))

start = time.time()

while True:
    data = stream.read(CHUNK)
    data = np.frombuffer(data, np.int16)
    line.set_ydata(data)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.01)

    if (time.time() - start) == 1:
        sample = np.frombuffer(data, np.int16)
        fft_data = fft(sample)
        freq = np.fft.fftfreq(len(fft_data))
        fig2 = plt.figure()
        fig2.plot(freq, fft_data)
        fig2.savefig('test.png')

    if (time.time() - start) > 10:
        break