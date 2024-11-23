import matlab.engine

def execute_matlab_function():
    # Start MATLAB engine
    eng = matlab.engine.start_matlab()

    try:
        eng.addpath('C://Users//saurabh nale//Desktop//production//imagegen//')

        # Change the current folder to the one containing the function
        eng.cd('C://Users//saurabh nale//Desktop//production//imagegen//')
        
        # Call your MATLAB function
        eng.ecg2cwt(nargout=0)

    except matlab.engine.MatlabExecutionError as e:
        print("Error executing MATLAB function:", e)

    finally:
        # Stop MATLAB engine
        eng.quit()

# Execute the MATLAB function
execute_matlab_function()
