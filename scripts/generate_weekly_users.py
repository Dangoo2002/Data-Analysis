import pandas as pd
import os

def generate_weekly_users():
    data = {
        'WEEK': pd.to_datetime(['2022-05-02 00:00:00.000', '2021-06-21 00:00:00.000', 
                                '2022-01-24 00:00:00.000', '2022-10-24 00:00:00.000', 
                                '2021-11-22 00:00:00.000']),
        'UNIQUE_USERS': [1022941, 111253, 1225468, 369557, 649202]
    }
    df = pd.DataFrame(data)
    
    # Save to the data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(os.path.join(data_dir, 'weekly_users.csv'), index=False)
    print("Generated weekly_users.csv")

if __name__ == "__main__":
    generate_weekly_users()
