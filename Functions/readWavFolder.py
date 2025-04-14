import os
from scipy.io import wavfile
import glob

def readWavFolder(folderPath):
    fileFolder=[]
    sampleRateFolder=[]

    files = os.listdir(folderPath)
    for filename in glob.glob(os.path.join(folderPath, '*.wav')):
        samplerate, data = wavfile.read(filename)
        fileFolder.append(data)
        sampleRateFolder.append(samplerate)
    return sampleRateFolder,fileFolder,files