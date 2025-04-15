import numpy as np
from scipy.fft import fft


def spectrumFromSignal(signal, sample_rate):
    """
    Computes the magnitude spectrum of a signal and filters it within a specified frequency range.
    Parameters:
        signal (numpy.ndarray): A 2D array where the first column represents the signal data.
        sample_rate (float): The sampling rate of the signal in Hz.
    Returns:
        tuple:
            - spectrum (numpy.ndarray): The magnitude of the spectrum filtered between 150 Hz and 1000 Hz.
            - freqs (numpy.ndarray): The corresponding frequency bins filtered between 150 Hz and 1000 Hz.
    """
    spectrum = fft(signal[:, 0])  # Compute the FFT for the first column
    freqs = np.fft.fftfreq(len(spectrum), d=1/sample_rate)[:len(spectrum) // 2]  # Compute frequency bins
    spectrum = abs(spectrum[:len(spectrum) // 2])  # Compute magnitude of the spectrum

    # Filter the spectrum and frequencies between 150 Hz and 1000 Hz
    mask = (freqs >= 150) & (freqs <= 1000)
    return spectrum[mask], freqs[mask]