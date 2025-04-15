import numpy as np
from scipy.signal import hilbert

def envelope_from_signal(signal):
    """
    Calculate the envelope of a signal using the Hilbert transform.

    Parameters:
        signal (numpy.ndarray): The input signal.

    Returns:
        numpy.ndarray: The envelope of the signal.
    """
    # Apply the Hilbert transform to the signal
    analytic_signal = hilbert(signal)
    
    # Calculate the envelope as the magnitude of the analytic signal
    envelope = np.abs(analytic_signal)
    
    return envelope
