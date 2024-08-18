import pandas as pd
import os
import random

def generate_weekly_new_users():
    data = {
        'NEW_USERS': [random.randint(1000, 300000) for _ in range(100)],
        'WEEK': pd.date_range(start='2021-01-01', periods=100, freq='W-MON')
    }
    df = pd.DataFrame(data)
    

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(os.path.join(data_dir, 'weekly_new_users.csv'), index=False)
    print("Generated weekly_new_users.csv")

if __name__ == "__main__":
    generate_weekly_new_users()
