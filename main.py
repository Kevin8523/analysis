import pandas as pd
import numpy as np
import os, sys
filename = '/users/kevin8523/desktop/github/coffee_consulting/data/2014.csv'
# Note: This code was developed using Anaconda 4.5.3 with Python 3.6.5
"""
# Notes / tricks learned from this project
1) .. = parent directory
2) __file__ path of where the script is located
    a. sys.path.append(os.path.join(os.path.dirname('__file__'), "lib"))
    b. script_path = os.path.dirname(os.path.abspath( __file__ ))
"""

data = pd.read_csv(filename)




