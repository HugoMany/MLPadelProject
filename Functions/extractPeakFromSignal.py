import numpy as np
from scipy.signal import find_peaks


def extractPeakFromSignal(signal, smoothing=1, num_peaks=None):
    # Ensure the signal is a 1-D array
    signalFile = signal.flatten()
    
    # Smooth the signal using a moving average filter
    window_size = smoothing  # Define the window size for smoothing
    smoothed_signal = np.convolve(signalFile, np.ones(window_size)/window_size, mode='same')
    signalFile = smoothed_signal

    # Find peaks in the signal
    peaks, properties = find_peaks(signalFile, height=10)
    
    # If num_peaks is specified, select the top N peaks based on height
    if num_peaks is not None:
        sorted_indices = np.argsort(properties["peak_heights"])[-num_peaks:]
        peaks = peaks[sorted_indices]
        properties["peak_heights"] = properties["peak_heights"][sorted_indices]
    
    return peaks, properties