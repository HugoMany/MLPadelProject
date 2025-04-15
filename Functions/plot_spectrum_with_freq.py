import matplotlib.pyplot as plt

def plot_spectrum_with_freq(signal, freqs, title="Spectrum Plot"):
    """
    Plots the spectrum of a signal against its corresponding frequencies.
    Parameters:
    signal (array-like): The spectrum of the signal (complex or real values).
    freqs (array-like): The frequencies corresponding to the spectrum values.
    title (str, optional): The title of the plot. Defaults to "Spectrum Plot".
    Returns:
    None: This function displays the plot and does not return any value.
    """
    magnitude = abs(signal)  # Compute magnitude of the spectrum

    plt.figure(figsize=(10, 6))
    plt.plot(freqs, magnitude)
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.show() 