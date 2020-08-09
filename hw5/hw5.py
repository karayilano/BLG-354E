#!/usr/bin/env python
# coding: utf-8

# In[204]:


import scipy.io.wavfile as wavfile
import scipy
from scipy import signal as sg
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt


# In[361]:


s_rate, signalAfrica = wavfile.read('Africa.wav')
s_rate, signalWinner = wavfile.read('WinnerTakesAll.wav')


# In[362]:


def ffthelper(signal):
    #abs since it contains complex numbers 
    FFT = FFT = abs(scipy.fft(signal))
    #normalization
    FFT = FFT * (1/len(FFT))
    freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))
    return FFT, freqs


# In[410]:


fftAfrica, freqsAfrica = ffthelper(signalAfrica)
fftWinner, freqsWinner = ffthelper(signalWinner)


# In[364]:


def plotter(fft, freqs):
    plt.plot(freqs[range(len(fft)//2)], fft[range(len(fft)//2)]) #we just need half of the spectrum
    plt.xlabel("Freq (Hz)")
    plt.ylabel("Amplitude")
    plt.show()


# In[365]:


plotter(fftAfrica, freqsAfrica) #fft spectrum of africa


# In[366]:


plotter(fftWinner, freqsWinner) #fft spectrum of winner 


# In[367]:


def cut(data, s_rate, start):
    #cut 256 point sample from the start(second)
    return data[(start*s_rate):((start*s_rate)+256)]


# In[436]:


sample1_africa = cut(signalAfrica, s_rate, 10)
sample2_africa = cut(signalAfrica, s_rate, 20)
sample3_africa = cut(signalAfrica, s_rate, 30)
sample1_winner = cut(signalWinner, s_rate, 10)
sample2_winner = cut(signalWinner, s_rate, 20)
sample3_winner = cut(signalWinner, s_rate, 30)

fftAfrica_sample1, freqsAfrica_sample1 = ffthelper(sample1_africa)
fftAfrica_sample2, freqsAfrica_sample2 = ffthelper(sample2_africa)
fftAfrica_sample3, freqsAfrica_sample3 = ffthelper(sample3_africa)
fftWinner_sample1, freqsWinner_sample1 = ffthelper(sample1_winner)
fftWinner_sample2, freqsWinner_sample2 = ffthelper(sample2_winner)
fftWinner_sample3, freqsWinner_sample3 = ffthelper(sample3_winner)


# In[437]:


#fftAfrica_sample1
x = [fftAfrica[i:i + 256] for i in range(0, len(fftAfrica), 256)]
arr = []
for j in range(len(x)):
    total = 0
    for i in range(len(x[j])):
        total = total + x[j][i] * fftAfrica_sample1[i]
    arr.append(total)
plt.plot(arr)
plt.show()


# In[439]:


plt.plot(arr[661:1061])


# In[440]:


#fftAfrica_sample2
arr = []
for j in range(len(x)):
    total = 0
    for i in range(len(x[j])):
        total = total + x[j][i] * fftAfrica_sample2[i]
    arr.append(total)
plt.plot(arr)
plt.show()


# In[441]:


plt.plot(arr[1522:1922])


# In[442]:


#fftAfrica_sample3
arr = []
for j in range(len(x)):
    total = 0
    for i in range(len(x[j])):
        total = total + x[j][i] * fftAfrica_sample3[i]
    arr.append(total)
plt.plot(arr)
plt.show()


# In[443]:


plt.plot(arr[2383:2783])


# In[447]:


#fftWinner_sample1
x = [fftWinner[i:i + 256] for i in range(0, len(fftWinner), 256)]
arr = []
for j in range(len(x)):
    total = 0
    for i in range(len(x[j])):
        total = total + x[j][i] * fftWinner_sample1[i]
    arr.append(total)
plt.plot(arr)
plt.show()


# In[448]:


plt.plot(arr[661:1061])


# In[449]:


#fftWinner_sample2
arr = []
for j in range(len(x)):
    total = 0
    for i in range(len(x[j])):
        total = total + x[j][i] * fftWinner_sample2[i]
    arr.append(total)
plt.plot(arr)
plt.show()


# In[450]:


plt.plot(arr[1522:1922])


# In[452]:


#fftWinner_sample3
arr = []
for j in range(len(x)):
    total = 0
    for i in range(len(x[j])):
        total = total + x[j][i] * fftWinner_sample3[i]
    arr.append(total)
plt.plot(arr)
plt.show()


# In[453]:


plt.plot(arr[2383:2783])


# In[ ]:





# In[ ]:




