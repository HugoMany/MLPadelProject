import numpy as np
from scipy.signal import find_peaks


def extractPeakFromSignal(signal, smoothing=1, num_peaks=None):
    """
    Extracts peaks from a 1-D signal array, with optional smoothing and peak selection.
    Parameters:
    -----------
    signal : array-like
        The input signal from which peaks are to be extracted. Must be a 1-D array.
    smoothing : int, optional
        The window size for applying a moving average filter to smooth the signal. 
        Default is 1 (no smoothing).
    num_peaks : int, optional
        The number of top peaks to return based on their height. If None, all detected 
        peaks are returned. Default is None.
    Returns:
    --------
    peaks : ndarray
        Indices of the detected peaks in the signal.
    properties : dict
        A dictionary containing properties of the detected peaks, such as their heights.
        The key "peak_heights" contains the heights of the detected peaks.
    Notes:
    ------
    - The function uses a moving average filter for smoothing the signal.
    - Peaks are detected using the `find_peaks` function from `scipy.signal`.
    - If `num_peaks` is specified, only the top `num_peaks` peaks (based on height) 
      are returned.
    Example:
    --------
    >>> import numpy as np
    >>> from scipy.signal import find_peaks
    >>> signal = np.array([0, 1, 2, 1, 0, 1, 3, 1, 0])
    >>> peaks, properties = extractPeakFromSignal(signal, smoothing=2, num_peaks=2)
    >>> print(peaks)
    >>> print(properties["peak_heights"])
    """
    # Ensure the signal is a 1-D array
    signalFile = signal.flatten()
    
    # Smooth the signal using a moving average filter
    window_size = smoothing  # Define the window size for smoothing
    smoothed_signal = np.convolve(signalFile, np.ones(window_size)/window_size, mode='same')
    signalFile = smoothed_signal

    # Find peaks in the signal
    peaks, properties = find_peaks(signalFile, height=10)
    
    # If num_peaks is specified, select the top N peaks based on height
    if num_peaks is not None:
        sorted_indices = np.argsort(properties["peak_heights"])[-num_peaks:]
        peaks = peaks[sorted_indices]
        properties["peak_heights"] = properties["peak_heights"][sorted_indices]
    
    return peaks, properties