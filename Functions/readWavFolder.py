import os
from scipy.io import wavfile
import glob

def readWavFolder(folderPath):
    """
    Reads all .wav files in the specified folder and returns their sample rates, 
    audio data, and filenames.
    Args:
        folderPath (str): The path to the folder containing .wav files.
    Returns:
        tuple: A tuple containing:
            - sampleRateFolder (list): A list of sample rates for each .wav file.
            - fileFolder (list): A list of numpy arrays containing the audio data for each .wav file.
            - files (list): A list of all filenames in the folder.
    Example:
        >>> sampleRates, audioData, filenames = readWavFolder("path/to/folder")
        >>> print(sampleRates)
        [44100, 48000]
        >>> print(filenames)
        ['file1.wav', 'file2.wav']
    """
    fileFolder=[]
    sampleRateFolder=[]

    files = os.listdir(folderPath)
    for filename in glob.glob(os.path.join(folderPath, '*.wav')):
        samplerate, data = wavfile.read(filename)
        fileFolder.append(data)
        sampleRateFolder.append(samplerate)
    return sampleRateFolder,fileFolder,files