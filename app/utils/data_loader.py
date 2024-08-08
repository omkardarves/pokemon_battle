import pandas as pd
import numpy as np

def load_data(filepath: str):
    data = pd.read_csv(filepath)
    
    # Replace problematic float values with finite numbers
    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    data.fillna(0, inplace=True)
    
    return data
