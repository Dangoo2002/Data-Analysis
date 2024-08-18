import pandas as pd
import os
import random

def generate_program_flipside_labels():
    data = {
        'BLOCKCHAIN': ['solana'] * 100,
        'CREATOR': ['flipside'] * 100,
        'ADDRESS': [f'Gov{random.randint(100000, 999999)}{random.choice(["L", "G", "H", "T"])}{random.randint(100000, 999999)}' for _ in range(100)],
        'LABEL_TYPE': ['dapp'] * 50 + ['nft'] * 25 + ['defi'] * 25,
        'LABEL_SUBTYPE': ['governance'] * 50 + ['marketplace'] * 25 + ['pool'] * 25,
        'LABEL': ['realms'] * 50 + ['solsea'] * 25 + ['solfarm'] * 25,
        'ADDRESS_NAME': ['realms general contract'] * 20 + ['psy finance'] * 20 + ['mango dao'] * 10 + 
                        ['Solsea NFT Marketplace'] * 25 + ['SOLfarm Vault'] * 25
    }
    df = pd.DataFrame(data)
    

    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(os.path.join(data_dir, 'program_flipside_labels.csv'), index=False)
    print("Generated program_flipside_labels.csv")

if __name__ == "__main__":
    generate_program_flipside_labels()
