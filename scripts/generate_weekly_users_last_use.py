import pandas as pd
import os
import random

def generate_weekly_users_last_use():
    data = {
        'LAST_USE': pd.date_range(start='2020-10-07', periods=100, freq='W-WED').strftime('%Y-%m-%d').tolist(),
        'ADDRESS': [random.randint(100, 10000) for _ in range(100)]
    }
    df = pd.DataFrame(data)
    
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(os.path.join(data_dir, 'weekly_users_last_use.csv'), index=False)
    print("Generated weekly_users_last_use.csv")

if __name__ == "__main__":
    generate_weekly_users_last_use()
