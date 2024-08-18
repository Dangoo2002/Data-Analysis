import pandas as pd
import os
import random

def generate_weekly_new_program():
    data = {
        'WEEK': pd.to_datetime(['2021-01-18', '2021-04-12', '2021-08-16', '2022-10-17', '2021-03-22']),
        'New Programs': [random.randint(1, 100) for _ in range(5)]
    }
    df = pd.DataFrame(data)
    

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(os.path.join(data_dir, 'weekly_new_program.csv'), index=False)
    print("Generated weekly_new_program.csv")

if __name__ == "__main__":
    generate_weekly_new_program()
