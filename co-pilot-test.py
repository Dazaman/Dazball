import numpy as np

# Import the co-pilot module
import co_pilot as cp

# Write function to add two numbers
def add(x, y): 
    return x + y

# Write function to read csv file and populate a dataframe
def read_csv(filename):
    # Read the csv file
    df = cp.read_csv(filename)
    # Return the dataframe
    return df
