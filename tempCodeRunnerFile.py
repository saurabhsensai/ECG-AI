from flask import Flask, render_template, jsonify, request
import serial.tools.list_ports
import subprocess
import matlab.engine
import numpy as np
import pandas as pd
import time

app = Flask(__name__)


def is_arduino_connected():
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'Arduino' in p.description  
    ]

    return bool(arduino_ports)



@app.route('/')
def index():
    return render_template('chart.html')

@app.route('/check_arduino_connection')
def check_arduino_connection():
    connected = is_arduino_connected()
    return jsonify({'connected': connected})

@app.route('/run_script')
def execute_script():
    # Assuming your script is named 'your_script.py'
    subprocess.run(['python', 'record.py'])
    
    return True


@app.route('/rrinter')
def rrinterval():
   
    
    # Assuming your script is named 'your_script.py'
    eng = matlab.engine.start_matlab()

    try:
    # Load ECG signal from CSV file
        eng.addpath('C://Users//saurabh nale//Desktop//ecgsite//') 
        eng.cd('C://Users//saurabh nale//Desktop//ecgsite//')
        # Call the MATLAB function
        y_filt = eng.rrinterval()
        print(y_filt["avg_rr_intervals"]) 
    finally:
    # Stop MATLAB Engine
        eng.quit()
    data = {"RR": int(y_filt["avg_rr_intervals"]), "heart": int(y_filt["hbpermin"]), "SD": int(y_filt["std_value"])}
    return jsonify(data)


@app.route('/customfile', methods=['GET', 'POST'])
def custfile():
    
    data = request.get_json()

    # Extract information from the received data
    name = data.get('inputString', '')
    print(name)
   # Assuming your script is named 'your_script.py'
    eng = matlab.engine.start_matlab()

    try:
    # Load ECG signal from CSV file
        eng.addpath('C://Users//saurabh nale//Desktop//ecgsite//') 
        eng.cd('C://Users//saurabh nale//Desktop//ecgsite//')
        # Call the MATLAB function
        y_filt = eng.rrforupload(name)
        print(y_filt["avg_rr_intervals"]) 
    finally:
    # Stop MATLAB Engine
        eng.quit()
    data = {"RR": int(y_filt["avg_rr_intervals"]), "heart": int(y_filt["hbpermin"]), "SD": int(y_filt["std_value"])}
    return jsonify(data)
    
    
    
    
    
    
    

if __name__ == '__main__':
    app.run(debug=True)


