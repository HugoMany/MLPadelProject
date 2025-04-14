from scipy.fft import fft

def spectrumFromWav(wavFile,):
    spectrum = fft(wavFile[:, 1]) # Compute the FFT for the first channel
    return abs(spectrum[:len(spectrum) // 2]) # Return the magnitude of the spectrum (half due to symmetry)