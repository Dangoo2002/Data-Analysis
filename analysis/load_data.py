import pandas as pd
import os

def load_data():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    
    # Load datasets from the generated CSVs
    flipside_labels = pd.read_csv(os.path.join(data_dir, 'program_flipside_labels.csv'))
    solana_fm_labels = pd.read_csv(os.path.join(data_dir, 'program_solana_fm_labels.csv'))
    days_active = pd.read_csv(os.path.join(data_dir, 'weekly_days_active.csv'))
    days_since_last_use = pd.read_csv(os.path.join(data_dir, 'weekly_days_since_last_use.csv'))
    new_program = pd.read_csv(os.path.join(data_dir, 'weekly_new_program.csv'))
    new_users = pd.read_csv(os.path.join(data_dir, 'weekly_new_users.csv'))
    program_data = pd.read_csv(os.path.join(data_dir, 'weekly_program.csv'))
    users_data = pd.read_csv(os.path.join(data_dir, 'weekly_users.csv'))
    users_last_use = pd.read_csv(os.path.join(data_dir, 'weekly_users_last_use.csv'))

    return {
        'flipside_labels': flipside_labels,
        'solana_fm_labels': solana_fm_labels,
        'days_active': days_active,
        'days_since_last_use': days_since_last_use,
        'new_program': new_program,
        'new_users': new_users,
        'program_data': program_data,
        'users_data': users_data,
        'users_last_use': users_last_use
    }

if __name__ == "__main__":
    data = load_data()
    for name, df in data.items():
        print(f"{name} data preview:")
        print(df.head(), "\n")
