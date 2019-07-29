# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:32:06 2019
"Filtering the 
@author: slabid
"""
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def scale(X, x_min, x_max):
    nom = (X-X.min(axis=0))*(x_max-x_min)
    denom = X.max(axis=0) - X.min(axis=0)
    #denom[denom==0] = 1
    return x_min + nom/denom 

def lowpassFilter(meanGrayLevels, fps): #add param video_path
    order = 4      #4
    cutoff = 0.05;  # desired cutoff frequency of the filter, Hz 0.05
    B, A = signal.butter(order, cutoff, output='ba')
    smooth_data = signal.filtfilt(B,A, meanGrayLevels)
    timestamp = np.arange(len(meanGrayLevels))/fps #in milliseconds
    
    #Normalizing data scaling between [-1, 1]
    MLG = np.asarray(meanGrayLevels)
    SD = np.asarray(smooth_data)
    MGL_scaled = scale(MLG,-1,1)
    SD_scaled = scale(SD, -1,1)
    
    #Plot configurations
    plt.subplot(2, 1, 1)
    plt.plot(timestamp, MGL_scaled, '-y', timestamp, SD_scaled, 'b-')
    plt.xlabel('Time (sec)')
    plt.ylabel('Mean gray value')
    locs, labels = plt.xticks()
    plt.xticks(np.arange(0, (len(meanGrayLevels)/fps), step=10))
    plt.show()
    
    return smooth_data
