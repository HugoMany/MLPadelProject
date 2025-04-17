import numpy as np

def attack_time_from_signal(signal, sample_rate, threshold=0.9):
    """
    Calculate the attack time of a signal based on its amplitude envelope.
    Parameters:
    signal (array-like): The spectrum of the signal (complex or real values).
    sample_rate (int): The sample rate of the signal in Hz.
    threshold (float): The threshold for determining the attack time as a fraction of the peak amplitude. Default is 0.9.
    Returns:
    attack_time (float): The attack time in seconds.
    """
    # Ensure the signal is a 1-D array
    signal = signal.flatten()

    # Find the peak amplitude
    peak_amplitude = np.max(signal)

    # Find the index where the signal first reaches the threshold of the peak amplitude
    attack_index = np.argmax(signal >= threshold * peak_amplitude)

    # Calculate the attack time in seconds
    attack_time = attack_index / sample_rate

    return attack_time