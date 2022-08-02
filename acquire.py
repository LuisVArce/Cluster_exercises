# importing needed libraries/modules
import os
import pandas as pd
import numpy as np

# importing visualization libraries 
import seaborn as sns
import matplotlib.pyplot as plt

# importing sql 
import env
from env import user, password, host 

def get_conn():
    db = 'zillow'
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'
    return url

def get_zillow(use_cache = True):
    
    zillow_file = 'zillow.csv'
    
    if os.path.exists(zillow_file) and use_cache:
        
        print('Status: Acquiring data from cached csv file..')
        
        return pd.read_csv(zillow_file)
        