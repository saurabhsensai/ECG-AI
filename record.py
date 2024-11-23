from serial.tools import list_ports
import serial
import time
import csv
import pandas as pd
import numpy as np
import scipy.fftpack    
import scipy.signal as signal
import matplotlib.pyplot as plt
import time      
import serial
import csv


arduino_port = 'COM10'  
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)


csv_filename = 'data.csv'
csv_file = open(csv_filename, 'w', newline='')
csv_writer = csv.writer(csv_file)

start_time = time.time()
record_duration = 10  

try:
    while time.time() - start_time < record_duration:
        
        line = ser.readline().decode('utf-8').strip()
        if line:
          
            data = line.split(',')
            csv_writer.writerow(data)
            
finally:
    ser.close()
    csv_file.close()

        

def filter_ecg(ecg_signal, fs=380, lowpass_cutoff=50, fir_cutoff=4):
  
    N = len(ecg_signal)
  
    T = 1.0 / fs
    
    x = np.linspace(0.0, N*T, N)
   
    yf = scipy.fftpack.fft(ecg_signal)
   
    xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))
   
    b, a = signal.butter(4, lowpass_cutoff/(fs/2), 'low')
    tempf = signal.filtfilt(b, a, ecg_signal)
    
    nyq_rate = fs/2.0
    width = 5.0/nyq_rate
    ripple_db = 60.0
    O, beta = signal.kaiserord(ripple_db, width)
    taps = signal.firwin(O, fir_cutoff/nyq_rate, window=('kaiser', beta), pass_zero=False)
    y_filt = signal.lfilter(taps, 1.0, tempf)
    return y_filt

     
dataset = pd.read_csv("data.csv")
y = [e for e in dataset.iloc[:, 0]]



filtered_signal = filter_ecg(y)

filtered_signal = np.array(filtered_signal)
filtered_signal = filtered_signal.astype(int)
filtered_signal =filtered_signal[160:]


csv_filename = 'static/recording.csv'

np.savetxt(csv_filename, filtered_signal, delimiter=',')


