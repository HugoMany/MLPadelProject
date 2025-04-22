# Characterization of padel ball/racket impact using artificial intelligence methods
*Junia ISEN – Master 1 project under the supervision of Arthur PATÉ*

25th November - 20th December 2024 ➡️ Research Part

17th March - 25th April 2025 ➡️ Application Part

### 👥 Authors:
ANTONIUK Pavlo, DAMERY Vincent, LAMBERT Edouard, MANY Hugo, OMS Henri, ZAKI Ilias

# 📑 Table of Contents

1. [🎯 Project Objective](#project-objective)  
2. [✨ Features](#features)  
3. [🤖 Machine Learning Models](#machine-learning-models)  
4. [📊 Data](#data)  
5. [🛠️ Tools and Functions](#tools-and-functions)  
6. [📁 Project Structure](#project-structure)  
7. [📊 Results and Evaluation](#results-and-evaluation)  


## 🎯Project Objective
The goal of this project is to predict the impact **position** of the ball on the padel racket, the **type** of racket used, and the racket’s **age**, based **sound** or **vibrations**.

## ✨Features 

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

## 🤖Machine Learning Models
### KNN
KNN is a simple model. It looks at the closest examples and choose the most common label. We used it as a baseline.

### RTF
Random Forest builds a bunch of decision trees and combines their results. it's a good model  for noise and avoids overfitting.

### SVM
SVM tries to find the best boundary to separate classes. It's a good model when the data has many features.

### XGBoost
XGBoost builds trees one at a time. Each new tree focuses on fixing the errors from the last one. It’s fast and mostly gives strong results.

## 📊Data
The dataset consists of audio and vibration recordings of padel ball impacts on rackets. The data is categorized based on the following attributes :

- **Racket Types**:  
    Four types of rackets are used, each differing in size, shape, number of holes, and other characteristics :  
    - **B** : Blue
    - **O** : Orange
    - **R** : Red
    - **V** : Green

- **Impact Zones**:  
    The ball impacts are recorded at three distinct zones of impact on the racket :  
    - **S** : Smash  
    - **C** : Center
    - **V** : Volley

- **Racket Generations**:  
    The rackets are categorized into three generations based on their time of use :  
    - **P1** : New rackets (Fixed condition)
    - **P2** : Moderately used rackets (Free condition)
    - **P3** : Heavily used rackets (Free condition)

For each combination of racket type, impact zone, and condition, 9 impacts are recorded.

This structured dataset provides a comprehensive basis for analyzing the relationship between sound/vibration features and racket characteristics.

### Sound
We use the sound data in temporal and frequency domains to extract features for the different models. The Fast Fourier Transform (FFT) was used to compute the spectrum.

Each audio file is named using the following format : `generation_racketType_numOfRecord_zoneOfImpact_numOfTry.wav`

Example : `P1_RB_1_C_1.wav`

### Vibration
We use the frequential data in frequency domain to extract features for the different models, using Fast Fourier Transform (FFT) to compute the spectrum.

The vibration datas are stored in the `All_Data_combined.csv` file. Below is an overview of the columns in this file :

| **Column Name**   | **Description**                                                              |
|------------------:|:-----------------------------------------------------------------------------|
| `Raw Signal Ch0`  | Temporal signal data captured from the vibration sensor.                     |
| `Spectrum`        | Frequency domain representation of the vibration signal.                     |
| `freqs`           | Frequency values corresponding to the spectrum data.                         |
| `File Name`       | Name of the file containing the recorded vibration data. `generation_racketType_numOfRecord_zoneOfImpact_numOfTry.csv`                                      |
| `Position`        | Impact zone on the racket where the ball made contact (C, S, V).             |
| `Racket Type`     | Color-coded identifier for the type of racket used (B, O, R, V).             |
| `Age`             | Generation or usage condition of the racket (P1, P2, P3).                    |



## 🛠️Tools and Functions


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




## 📁Project Structure


```
├── Data
├── Functions
├── SoundPart
│   ├── ModelMLAgeRacket
│   │   ├── KNN
│   │   |   ├── S_KNN_Age_P1.P2.P3_Peaks.ipynb
│   │   |   ├── S_KNN_Age_P1.P2.P3_Peaks.csv
│   │   |   ├── xxxx.ipynb
│   │   |   └── xxxx.csv
│   │   └── RTF
│   ├── ModelMLPositionRacket
│   └── ModelMLTypeRacket
├── VibrationPart
│   ├── Deprecated
│   ├── ModelMLAgeRacket
│   ├── ModelMLPositionRacket
│   └── ModelMLTypeRacket
└── Visualization
```

## 📊Results and Evaluation

The best results for each model are stored in the `AllResults.xlsx` file. All of them was trained and tested on sound and vibration datasets with selected features to evaluate its effectiveness.

The file contains multiple sheets : sound, vibration, both, comparisons between sound and vibration and comparison between KNN and RTF.

The table below show some example of performance for different machine learning models from this file  :

> Sound

| **Model Type** | **Objectives** | **Dataset** | **Features** | **Training Accuracy** | **Test Accuracy** |
|:--------------:|:--------------:|:-----------:|:------------:|:---------------------:|:-----------------:|
| `KNN`          | Position       | P1          | Energy       | 99.7%                 | 100%              |
| `KNN`          | Age            | P1.P2.P3    | Peaks        | 100%                  | 77.3%             |
| `RTF`          | Age            | P1.P2.P3    | Peaks        | 99.8%                 | 91.4%             |
| `RTF`          | Racket Type    | P1.P2.P3    | AttackTime   | 100%                  | 67.5%             |
| ...            | ...            | ...         | ...          | ...                   | ...               |

> Vibration

| **Model Type** | **Objectives** | **Dataset** | **Features** | **Training Accuracy** | **Test Accuracy** |
|:--------------:|:--------------:|:-----------:|:------------:|:---------------------:|:-----------------:|
| `KNN`          | Position       |	P1      	  | Envelope	   | 99.4%                 | 100%              |
| `KNN`          | Racket Type    |	P1.P2.P3 	  | MFCC    	   | 100%                  | 100%              |
| `RTF`          | Position       |	P1      	  | Energy	     | 100%                  | 95.5%             |
| ...            | ...            | ...         | ...          | ...                   | ...               |