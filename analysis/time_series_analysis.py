import pandas as pd
import matplotlib.pyplot as plt
import os

def time_series_analysis(new_users):
  
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    

    new_users.to_csv(os.path.join(output_dir, 'time_series_data.csv'), index=False)
    
    plt.figure(figsize=(12, 6))
    plt.plot(new_users['WEEK'], new_users['NEW_USERS'], label='New Users')
    plt.xlabel('Week')
    plt.ylabel('Number of New Users')
    plt.title('Weekly New Users Over Time')
    plt.legend()
    
   
    plt.savefig(os.path.join(output_dir, 'time_series_plot.png'))
    plt.close()

    print("Time series analysis complete. Data and plot saved to 'output/time_series_data.csv' and 'output/time_series_plot.png'.")

if __name__ == "__main__":
    from load_data import load_data
    from clean_data import clean_data
    
    data = load_data()
    cleaned_data = clean_data(data)
    
    time_series_analysis(cleaned_data['new_users'])
