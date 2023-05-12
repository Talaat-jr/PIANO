import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

t = np.linspace(0, 3 ,(3*1024))

C3 = 130.81
D3 = 146.83
E3 = 164.81
F3 = 174.61
G3 = 196
A3 = 220
B3 = 246.93

f3 = [130.81,146.83,164.81,174.61,196,220,246.93]

f4 = [261.63,293.66,329.63,349.23,392,440,493.88]

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392
A4 = 440
B4 = 493.88

notes = [
    [ 65.41, 130.81, 261.63, 523.25],  # C
    [ 73.42, 146.83, 293.66, 587.33],  # D
    [ 82.41, 164.81, 329.63, 659.25],  # E
    [ 87.31, 174.61, 349.23, 698.46],  # F
    [ 98.00, 196.00, 392.00, 783.99],  # G
    [110.00, 220.00, 440.00, 880.00],  # A
    [123.47, 246.94, 493.88, 987.77],  # B
]


def generate_song(time,number_Of_Notes):
    octave1 = []
    octave2 = []
    for i in range (number_Of_Notes):
        index1 , index2 = np.random.randint(0,len(f3)-1, 2)
        octave1 += [f3[index1]]
        octave2 += [f4[index2]]
    
    s1 = np.sin(2*np.pi*octave1*time)
    s2 = np.sin(2*np.pi*octave2*time)
    return s1 , s2

    
    

duration = 3

T = 0.5

x =( (np.sin(2 * np.pi * C3*t )+(np.sin(2*np.pi*C4*t))))


plt.plot(t, x)
sd.play(x,3*1024)





