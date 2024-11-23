
function y_filt = filter_ecg()
fs = 380;
lowpass_cutoff = 50;
fir_cutoff = 4;
csvFilename = '../raw/saurabh2.csv';
dataTable = readtable(csvFilename);
ecg_signal = dataTable{:, 1};
    N = length(ecg_signal);
    T = 1.0 / fs;
    
    % Time vector
    x = linspace(0.0, N * T, N);
    
    % Compute FFT
    yf = fft(ecg_signal);
    
    % Frequency vector
    xf = linspace(0.0, 1.0 / (2.0 * T), floor(N / 2));
    
    % Design low-pass FIR filter using fir1
    b = fir1(64, lowpass_cutoff / (fs / 2), 'low');
    
    % Apply zero-phase filtering using filtfilt
    tempf = filtfilt(b, 1, ecg_signal);
    
    % Design FIR filter with Kaiser window
    nyq_rate = fs / 2.0;
    width = 5.0 / nyq_rate;
    ripple_db = 60.0;
    
    % Corrected kaiserord call
    [O, ~, beta] = kaiserord([fir_cutoff/(nyq_rate/2) (lowpass_cutoff/(nyq_rate/2))], [1 0], [10^(-ripple_db/20) 10^(-60/20)]);
    
    taps = fir1(O, [fir_cutoff lowpass_cutoff] / nyq_rate, 'bandpass', kaiser(O + 1, beta));
    
    % Apply the second filter
    y_filt = filter(taps, 1.0, tempf);

    csvwrite('../filtered/saurabh2.csv', y_filt);



end
