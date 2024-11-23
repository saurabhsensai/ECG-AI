import matlab.engine
import numpy as np
import pandas as pd

# Start MATLAB Engine
eng = matlab.engine.start_matlab()

try:
    # Load ECG signal from CSV file
   
    eng.addpath('C://Users//saurabh nale//Desktop//production//rrinterval//')

     
    eng.cd('C://Users//saurabh nale//Desktop//production//rrinterval//')
    # Call the MATLAB function
    y_filt = eng.rrinterval()

    print(int(y_filt["avg_rr_intervals"]))
    print(int(y_filt["hbpermin"]))
    print(int(y_filt["std_value"]))


finally:
    # Stop MATLAB Engine
    eng.quit()
