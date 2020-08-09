#O.Kürşat Karayılan
#150140011

import numpy as np
import wave
import sys
import math
import contextlib

fname = 'WinnerTakesAll.wav'
outname = 'output.wav'

cutOffFrequency = 2000.0


def running_mean(x, windowSize):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize


def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved=True):
    dtype = np.int16

    channels = np.fromstring(raw_bytes, dtype=dtype)

    if interleaved:
        # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data
        channels.shape = (n_frames, n_channels)
        channels = channels.T
    else:
        # channels are not interleaved. All samples from channel M occur before all samples from channel M-1
        channels.shape = (n_channels, n_frames)

    return channels


with contextlib.closing(wave.open(fname, 'rb')) as spf:
    sampleRate = spf.getframerate()
    ampWidth = spf.getsampwidth()
    nChannels = spf.getnchannels()
    nFrames = spf.getnframes()

    # Extract Raw Audio from multi-channel Wav File
    signal = spf.readframes(nFrames * nChannels)
    spf.close()
    channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)

    # get window size
    freqRatio = (cutOffFrequency / sampleRate)
    N = int(math.sqrt(0.196196 + freqRatio ** 2) / freqRatio)

    # LPF
    filtered = running_mean(channels[0], N).astype(channels.dtype)

    # HPF
    # signal = channels[0]
    # filtered = signal[:-8] - filtered

    # writing to file
    wav_file = wave.open(outname, "w")
    wav_file.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
    wav_file.writeframes(filtered.tobytes('C'))
    wav_file.close()
