import pandas as pd
import os

def load_csv(filename):
    """
    Load a CSV file from the data directory.
    
    Args:
        filename (str): The name of the CSV file to load.
    
    Returns:
        pd.DataFrame: The loaded data as a Pandas DataFrame.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    
    file_path = os.path.join(data_dir, filename)
    
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {filename} not found in directory {data_dir}")
    
    return pd.read_csv(file_path)

if __name__ == "__main__":
    # Example usage: load the 'weekly_program.csv' file
    program_data = load_csv('weekly_program.csv')
    print("Program Data Preview:")
    print(program_data.head(), "\n")
    
    # Load additional data as needed
    users_data = load_csv('weekly_users.csv')
    print("Users Data Preview:")
    print(users_data.head(), "\n")
