# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:42:21 2019
#Function related to measure the breath rate in BPM (Breath Per Minute )
#after taking the number of respiratory cycles done in the whole video
@author: slabid
"""
import numpy as np
import itertools

def breathRates(smooth_data, total_frames, fps):
    a = np.diff(smooth_data)
    nb_breaths = round(len(list(itertools.groupby(a, lambda a: a > 0)))/2) #div. by 2 for down peaks w/o upper peaks.
    print('Le sujet a effectué '+str(nb_breaths) +' cycles respiratoires.')
    respiratory_bpm = round(nb_breaths/(total_frames/fps)*60)
    print('Le sujet a donc un rythme de '+str(respiratory_bpm) +' respirations par minute.')
    return respiratory_bpm