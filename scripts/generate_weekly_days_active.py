import pandas as pd
import os
import random
import numpy as np

def generate_weekly_days_active():
    data = {
        'CREATION_DATE': pd.date_range(start='2020-10-07', periods=100, freq='W-WED'),
        'Days Active': np.random.normal(150, 50, 100).tolist()
    }
    df = pd.DataFrame(data)
    
  
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(os.path.join(data_dir, 'weekly_days_active.csv'), index=False)
    print("Generated weekly_days_active.csv")

if __name__ == "__main__":
    generate_weekly_days_active()
