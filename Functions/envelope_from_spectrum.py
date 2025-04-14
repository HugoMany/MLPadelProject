import numpy as np

def envelope_from_spectrum_Vib(spectrum, freq_test, band_width):
    energy_per_band = []
    for i in range(0, len(freq_test), band_width):
        band_energy = np.sum(spectrum[i:i + band_width] ** 2)
        energy_per_band.append(band_energy)
    return energy_per_band