from scipy.fft import fft

def spectrumFromWav(wavFile,):
    spectrum = fft(wavFile[:, 1]) 
    return abs(spectrum[:len(spectrum) // 2])  