# Characterization of padel ball/racket impact using artificial intelligence methods
*Junia ISEN – Master 1 project under the supervision of Arthur PATÉ*

25th November - 20th December 2024 ➡️ Research Part

17th March - 25th April 2025 ➡️ Application Part

### 👥 Authors:
ANTONIUK Pavlo, DAMERY Vincent, LAMBERT Edouard, MANY Hugo, OMS Henri, ZAKI Ilias

# 📑 Table of Contents

1) 🎯 Project Objective  
2) ✨ Features  
3) 🤖 Machine Learning Models  
4) 📊 Data  
5) 🛠️ Tools & Functions  
6) 📊 Results and Evaluation 


## 🎯Project Objective
The goal of this project is to predict the impact **position** of the ball on the padel racket, the **type** of racket used, and the racket’s **age**, based **sound** or **vibrations**.

## ✨ Features 

### Energy
Energy per frequency band is extracted using the FFT and segmented using customizable bandwidths. This highlights how much energy is distributed across specific frequency regions.

### Envelope
The spectral envelope of the audio signal is calculated using the **Hilbert transform**. It captures how the amplitude change over time.

### MFCC
Mel-Frequency Cepstral Coefficients are extracted to represent the spectral content in a perceptually relevant way. Averaged MFCCs are used as features for classification tasks.

### Peaks
Using FFT, the most prominent frequency peaks (position and magnitude) are extracted from the audio signal. These peaks shows the dominant acoustic components of each impact.

### Attack Time
This feature represents the time it takes for the sound to rise from silence to its peak amplitude — a key characteristic in assessing impact sharpness and racket responsiveness.

## 🤖 Machine Learning Models
### KNN
KNN is a simple model. It looks at the closest examples and choose the most common label. We used it as a baseline.

### RTF
Random Forest builds a bunch of decision trees and combines their results. it's a good model  for noise and avoids overfitting.

### SVM
SVM tries to find the best boundary to separate classes. It's a good model when the data has many features.

### XGBoost
XGBoost builds trees one at a time. Each new tree focuses on fixing the errors from the last one. It’s fast and mostly gives strong results.

## 📊 Data 

### Sound
We recorded audio from real racket-ball hits. Then we used it to get features from the time and frequency domains (like FFT).

### Vibration
We also recorded vibration data using sensors. This gives us another way to understand the impact, along with the audio.


## 🛠️ Tools & Functions 

### Signal Processing Functions

- `readWavFolder(folderPath)`
  > Reads all `.wav` files from a folder and returns their sample rates, data arrays, and filenames.

- `spectrumFromWav(wavFile)`
  > Computes the FFT magnitude spectrum of the **first audio channel** of a WAV file.

- `spectrumFromSignal(signal, sample_rate)`
  > Computes the FFT magnitude spectrum and filters it between 150 Hz and 1000 Hz.

- `energy_per_frequency_band_from_spectrum(spectrum, freqs, band_width)`
  > Divides the frequency spectrum into bands and computes the energy (sum of squares) in each.

- `envelope_from_signal(signal)`
  > Computes the **amplitude envelope** of a 1D signal using the Hilbert transform.

- `extractPeakFromSignal(signal, smoothing=1, num_peaks=None)`
  > Extracts the most prominent peaks from a 1D signal, with optional smoothing and limit on number of peaks.

- `plot_spectrum_with_freq(signal, freqs, title="Spectrum Plot")`
  > Displays the magnitude of a frequency spectrum against its corresponding frequencies.

### Vibration Data Functions

- `readAllFileVibration(folderPath)`
  > Recursively loads all `.csv` vibration files from a directory and returns the folder name and the corresponding pandas DataFrame.




## 📁 Project Structure


```
├── Data
├── Functions
├── SoundPart
│   ├── ModelMLAgeRacket
│   │   ├── RTF
│   │   │   ├── S_RTF_Age_P1.P2.P3_Peaks.ipynb
│   │   │   ├── S_RTF_Age_P1.P2.P3_Peaks.csv
│   │   │   ├── xxxx.ipynb
│   │   │   └── xxxx.csv
│   │   ├── .....
│   ├── ModelMLPositionRacket
│   ├── ModelMLTypeRacket
├── VibrationPart
│   ├── Deprecated
│   ├── ModelMLAgeRacket
│   ├── ModelMLPositionRacket
│   ├── ModelMLTypeRacket
├── Visualization
```

## 📊 Results and Evaluation


