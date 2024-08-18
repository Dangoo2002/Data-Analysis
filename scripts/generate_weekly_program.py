import pandas as pd
import os
import random

def generate_weekly_program():
    data = {
        'WEEK': pd.to_datetime(['2022-05-30', '2022-03-14', '2022-04-04', '2021-05-03', '2021-04-12']),
        'UNIQUE_PROGRAMS': [random.randint(50, 1500) for _ in range(5)]
    }
    df = pd.DataFrame(data)
    
  
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(os.path.join(data_dir, 'weekly_program.csv'), index=False)
    print("Generated weekly_program.csv")

if __name__ == "__main__":
    generate_weekly_program()
