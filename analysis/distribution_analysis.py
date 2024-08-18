import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def distribution_analysis(users_last_use):
  
    print("Users Last Use Columns:", users_last_use.columns)
    
   
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    
    users_last_use.to_csv(os.path.join(output_dir, 'distribution_data.csv'), index=False)
    
    plt.figure(figsize=(12, 6))
  
    sns.histplot(users_last_use['LAST_USE'], kde=True)
    plt.title('Distribution of Last Use Dates for Users')
    plt.xlabel('Last Use Date')
    plt.ylabel('Frequency')
    

    plt.savefig(os.path.join(output_dir, 'distribution_plot.png'))
    plt.close()  

    print("Distribution analysis complete. Data and plot saved to 'output/distribution_data.csv' and 'output/distribution_plot.png'.")

if __name__ == "__main__":
    from load_data import load_csv


    users_last_use = load_csv('weekly_users_last_use.csv')
    
    distribution_analysis(users_last_use)
