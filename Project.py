import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

t=np.linspace(0,3,12*1024)

C3 = 130.81
D3 = 146.83
E3 = 164.81
F3 = 174.61
G3 = 196
A3 = 220
B3 = 246.93

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392
A4 = 440
B4 = 493.88

T = 0.5

x =(( (np.sin(2 * np.pi * c3 )+(np.sin(2*np.pi*c4)))*([t>=0 & t<=T]))



# x=(()+())

plt.plot(t,x)
sd.play(x,3*1024)