import pandas as pd
import numpy as np
import os, sys
path = '/users/kevin8523/desktop/github/coffee_consulting/data/'
filename = 'All.txt'
filepath = f'{path}{filename}'
# Note: This code was developed using Anaconda 4.5.3 with Python 3.6.5
"""
# Notes / tricks learned from this project
1) .. = parent directory
2) __file__ path of where the script is located
    a. sys.path.append(os.path.join(os.path.dirname('__file__'), "lib"))
    b. script_path = os.path.dirname(os.path.abspath( __file__ ))
3) Cmd + I for help on objects
4) #%% to create cells
"""
#%% Load the data into a DataFrame
df = pd.read_csv(filepath, sep='\t', header=0, encoding='latin-1')

print(df.shape)
df.head(5)
df.tail(5)
df.info()
df.describe()

#%% Feature Engineering 
df['Date']


#RCODE
#Create the Year/Month/Day
data$Date <- str_replace_all(data$Date, "/", "-")
data$Date <- mdy(data$Date)
which(is.na(data$Date))
data$Year <- year(data$Date)
data$Month <- month(data$Date)
data$Day <- day(data$Date)

#Create Times
data$Time <- hms(data$Time)
which(is.na(data$Time))
data$Hour <- hour(data$Time)
data$Minute <- minute(data$Time)
data$Second <- second(data$Time)

data$`Time Zone` <- NULL


