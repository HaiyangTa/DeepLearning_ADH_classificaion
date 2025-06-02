import numpy as np
from scipy.io import loadmat

def get_eeg_info(path):
    mat = loadmat(path)
    eeg = mat['transferred_EEG']
    # Extract the structure fields
    eeg_struct = eeg[0, 0]
    # info extraction.
    labels = [str(label[0]) for label in eeg_struct['label'][0]]
    fs = float(eeg_struct['fsample'][0][0])
    trial = eeg_struct['trial'][0]   # list of trials
    time  = eeg_struct['time'][0]    # list of time vectors
    eeg_data = trial[0]   # shape: [nChannels x nTimePoints]
    time_vec = time[0]    # shape: [nTimePoints]
    return {'time': time_vec, 'eeg_data': eeg_data, 'fs': fs, 'labels': labels}