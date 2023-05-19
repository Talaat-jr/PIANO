import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft

n = 3 * 1024
f = np.linspace(0,512,n//2)
t = np.linspace(0, 3,(12*1024))

notes = [261.63, 293.66, 329.63,349.23,392,440,493.88,261.63,233.08, 261.63, 277.18, 311.13, 349.23, 369.99, 415.30, 466.16]

def generate_Song (notes):
    
    note_duration = 3/(((3/2)*len(notes))-0.5)
    silence = note_duration/2
    t_start = 0
    t_end = note_duration
    x = 0
    for i in range(len(notes)):
        x += np.reshape(2*np.sin( 2 * np.pi * notes[i] * t) * [t>=t_start]*[t<=t_end], np.shape(t))
        t_start += note_duration+silence
        t_end += note_duration+silence
    return x
        
def generate_Noise():
    rand_noise_freq_1, rand_noise_freq_2 = np.random.randint(0, 512, 2)
    noiseGen = np.sin(2 * np.pi * rand_noise_freq_1 * t) + np.sin(2 * np.pi * rand_noise_freq_2 * t)
    return noiseGen


noise_gen = generate_Noise()


song_gen = generate_Song(notes)

song_freq= fft(song_gen)
song_freq = (2/n) * (np.abs(song_freq [0:int(n/2)]))

song_with_noise = noise_gen + song_gen

song_with_noise_freq = fft(song_with_noise)
song_with_noise_freq = (2/n) * (np.abs(song_with_noise_freq [0:int(n/2)]))


def detect_noise():
    max_frequency_magnitude = int(np.ceil(max(song_freq)))
    (noise_frequencies,) = np.where(song_with_noise_freq > max_frequency_magnitude)
    noise_detect=0
    for i in noise_frequencies:
        noise_frequencies = f[i]
        noise_detect += np.sin(2 * np.pi * np.round(noise_frequencies) * t)
    return noise_detect


noise_detect = detect_noise()


song_after_noise_cancelation = song_with_noise - noise_detect

song_after_noise_cancelation_freq = fft(song_after_noise_cancelation)
song_after_noise_cancelation_freq = (2/n) * (np.abs(song_after_noise_cancelation_freq [0:int(n/2)]))



# Plots:-

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(t,song_gen)

plt.subplot(3,1,2)
plt.plot(t,song_with_noise)

plt.subplot(3,1,3)
plt.plot(t,song_after_noise_cancelation)


plt.figure(2)
plt.subplot(3,1,1)
plt.plot(f,song_freq)

plt.subplot(3,1,2)
plt.plot(f,song_with_noise_freq)

plt.subplot(3,1,3)
plt.plot(f,song_after_noise_cancelation_freq)




sd.play(song_after_noise_cancelation,n)
