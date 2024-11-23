def filter_ecg(ecg_signal, fs=380, lowpass_cutoff=50, fir_cutoff=4):
    """
    Function to preprocess ECG signals by applying a low-pass Butterworth filter
    and a Finite Impulse Response (FIR) filter.

    Parameters:
    - ecg_signal: numpy array, ECG signal data
    - fs: int, sampling frequency (default: 380 Hz)
    - lowpass_cutoff: int, cutoff frequency for the low-pass Butterworth filter (default: 50 Hz)
    - fir_cutoff: int, cutoff frequency for the FIR filter (default: 4 Hz)

    Returns:
    - y_filt: numpy array, preprocessed ECG signal
    """

    N = len(ecg_signal)
    
    # Sample spacing
    T = 1.0 / fs
    # Compute x-axis
    x = np.linspace(0.0, N*T, N)
    # Compute FFT
    yf = scipy.fftpack.fft(ecg_signal)
    # Compute frequency x-axis
    xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))

    # Apply low-pass filter using Butterworth filter design
    b, a = signal.butter(4, lowpass_cutoff/(fs/2), 'low')
    tempf = signal.filtfilt(b, a, ecg_signal)

    # Apply FIR filter using Kaiser window design
    nyq_rate = fs/2.0
    width = 5.0/nyq_rate
    ripple_db = 60.0
    O, beta = signal.kaiserord(ripple_db, width)
    taps = signal.firwin(O, fir_cutoff/nyq_rate, window=('kaiser', beta), pass_zero=False)
    y_filt = signal.lfilter(taps, 1.0, tempf)

    return y_filt
