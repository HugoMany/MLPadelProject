from scipy.fft import fft

def spectrumFromWav(wavFile):
    """
    Simplified version of spectrumFromSignal, computes the magnitude spectrum 
    of the first channel of a WAV file without computing the frequencies.

    Parameters:
        wavFile (numpy.ndarray): A 2D NumPy array representing the WAV file data, 
                                 where each row corresponds to a sample and columns 
                                 represent audio channels.

    Returns:
        numpy.ndarray: A 1D NumPy array containing the magnitude of the spectrum 
                       for the first channel, limited to the first half of the 
                       spectrum due to symmetry.
    """
    spectrum = fft(wavFile[:, 0]) # Compute the FFT for the left channel
    return abs(spectrum[:len(spectrum) // 2]) # Return the magnitude of the spectrum (half due to symmetry)