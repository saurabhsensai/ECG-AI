
from flask import Flask, render_template, jsonify
import serial.tools.list_ports
import subprocess
import matlab.engine
import numpy as np
import pandas as pd
import time
    
    # Assuming your script is named 'your_script.py'
eng = matlab.engine.start_matlab()

try:
    # Load ECG signal from CSV file
    eng.addpath('C://Users//saurabh nale//Desktop//ecgsite//') 
    eng.cd('C://Users//saurabh nale//Desktop//ecgsite//')
        # Call the MATLAB function
    y_filt = eng.rrforupload("recording.csv")
    print(y_filt["avg_rr_intervals"]) 
finally:
    # Stop MATLAB Engine
    eng.quit()
data = {"RR": int(y_filt["avg_rr_intervals"]), "heart": int(y_filt["hbpermin"]), "SD": int(y_filt["std_value"])}
print(data)