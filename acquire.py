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
        query = '''
         SELECT bedroomcnt as bedroom_count, bathroomcnt as bath_count, 
                calculatedfinishedsquarefeet as finished_sq_feet, taxvaluedollarcnt as home_value, 
                 yearbuilt, fips        
        FROM properties_2017
        JOIN propertylandusetype using (propertylandusetypeid)
        JOIN predictions_2017 ON properties_2017.id = predictions_2017.id
        WHERE propertylandusetype.propertylandusedesc = "Single Family Residential"
        AND predictions_2017.transactiondate LIKE "2017%%"
        '''
    
    print('Status: Acquiring data from SQL database..')
    
    zillow = pd.read_sql(query, get_conn())
    
    print('Status: Saving zillow data locally..')
    
    zillow.to_csv(zillow_file, index = False)