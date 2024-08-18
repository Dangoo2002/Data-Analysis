import pandas as pd
import os
import random

def generate_program_solana_fm_labels():
    data = {
        'FriendlyName': ['Kamino Program', 'Francium Lending Reward Program', 'DeGods Bank', 'Port Finance Program', 'Lifinity Program'],
        'ADDRESS': [f'{random.choice(["6LtLpn", "3Katmm", "6VJpeY", "Port7u", "Eewxy"])}{random.randint(100000, 999999)}' for _ in range(5)],
        'Abbreviation': ['Kamino Program', 'Lending Reward', 'DeGods Bank', None, 'Lifinity Program'],
        'Category': ['programs'] * 5,
        'Flag': [None] * 5,
        'LogoURI': ['https://pbs.twimg.com/profile_images/156315488...' for _ in range(5)]
    }
    df = pd.DataFrame(data)
    
    # Save to the data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(os.path.join(data_dir, 'program_solana_fm_labels.csv'), index=False)
    print("Generated program_solana_fm_labels.csv")

if __name__ == "__main__":
    generate_program_solana_fm_labels()
