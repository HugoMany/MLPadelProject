import numpy as np

def envelope_from_spectrum(spectrum, freq_test, band_width):
	"""
	Calculate the envelope of a spectrum within a specified frequency band.

	Parameters:
		spectrum (numpy.ndarray): The input spectrum.
		freq_test (float): The center frequency to test.
		band_width (float): The width of the frequency band.

	Returns:
		numpy.ndarray: The envelope of the spectrum within the specified band.
	"""
	# Create a frequency mask for the specified band
	freq_mask = (spectrum >= freq_test - band_width / 2) & (spectrum <= freq_test + band_width / 2)
	
	# Apply the mask to extract the relevant part of the spectrum
	band_spectrum = spectrum[freq_mask]
	
	# Calculate the envelope (e.g., using the absolute value)
	envelope = np.abs(band_spectrum)
	
	return envelope
