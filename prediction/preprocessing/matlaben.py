import matlab.engine
import numpy as np
import pandas as pd

# Start MATLAB Engine
eng = matlab.engine.start_matlab()

try:
    # Load ECG signal from CSV file
   
    eng.addpath('C://Users//saurabh nale//Desktop//production//preprocessing//')

        # Change the current folder to the one containing the function
    eng.cd('C://Users//saurabh nale//Desktop//production//preprocessing//')
    # Call the MATLAB function
    y_filt = eng.filter_ecg()

    


finally:
    # Stop MATLAB Engine
    eng.quit()
