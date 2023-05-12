import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# t = np.linspace(0, 3,(9*1024))
t = np.linspace(0, 3,(12*1024))

notes = [261.63, 293.66, 329.63,349.23,392,440,493.88,261.63,233.08, 261.63, 277.18, 311.13, 349.23, 369.99, 415.30, 466.16]

def generate_Song (notes):
    note_duration = 0.1518987342
    silence = note_duration/4
    t_start = 0
    t_end = note_duration
    x = 0
    for i in range(16):
        x += np.reshape(np.sin( 2 * np.pi * notes[i] * t) * [t>=t_start]*[t<=t_end], np.shape(t))
        t_start += note_duration+silence
        t_end += note_duration+silence
    return x
    

def play_Song(x):
    plt.plot(t, x)
    # sd.play(x,4*1024)
    sd.play(x,3*1024)

x = generate_Song(notes)
play_Song(x)