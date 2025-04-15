import numpy as np

def energy_per_frequency_band_from_spectrum(spectrum, freqs, band_width):
    """
    Calculate the energy per frequency band from a given spectrum.
    This function divides the frequency range into bands of a specified width
    and computes the energy (sum of squared magnitudes) for each band. It also
    calculates the center frequency of each band.
    Parameters:
        spectrum (numpy.ndarray): The spectrum values (e.g., magnitudes or amplitudes).
        freqs (numpy.ndarray): The corresponding frequencies of the spectrum.
        band_width (int): The width of each frequency band.
    Returns:
        tuple:
            - band_energies (list): A list of energy values for each frequency band.
            - band_frequencies (list): A list of center frequencies for each band.

    Example :

    >>> band_energies, band_frequencies = energy_per_frequency_band_from_spectrum(spectrum, freqs, bd)

    >>> band_energies => the energy for each band
    >>> band_frequencies => frequency for each band

    """
    # Calculate energy per band
    band_energies = []
    band_frequencies = []
    for start_freq in range(0, int(freqs[-1]), band_width):
        end_freq = start_freq + band_width
        band_indices = np.where((freqs >= start_freq) & (freqs < end_freq))[0]
        band_energy = np.sum(spectrum[band_indices]**2)  # Sum of squared magnitudes
        band_energies.append(band_energy)
        band_frequencies.append((start_freq + end_freq) / 2)  # Center frequency of the band

    return band_energies, band_frequencies