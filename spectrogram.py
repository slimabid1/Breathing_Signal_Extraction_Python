# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 18:49:34 2019

@author: Slim
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy import signal as sig

def sigSpectrogram(signalx):
    fs = 256 # sample rate, Hz
#    signalx = np.array(signalx)
#    f, psd = sig.periodogram(signalx, fs, 'flattop', scaling='spectrum')
#
#    plt.subplot(2, 1, 2) 
#    plt.semilogy(f, psd)
#    plt.xlabel('frequency [Hz]')
#    plt.ylabel('PSD [V**2/Hz]')
#    plt.show
#
#    return powerSpectrum
    
    fig,axs = matplotlib.pyplot.subplots(ncols=1, nrows=2 )
    N=len(signalx)
    spectrum, freqs, t, im = axs[1].specgram(signalx, Fs=fs, cmap=matplotlib.cm.inferno,noverlap=255)
    axs[0].plot(np.arange(0,N)/fs,signalx,'-')
    axcb = fig.colorbar(im, ax=axs[1], pad=0.1, aspect = 20)