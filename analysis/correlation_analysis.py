import pandas as pd
import matplotlib.pyplot as plt
import os

def load_csv(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    return pd.read_csv(os.path.join(data_dir, file_name))

def correlation_analysis(days_active, new_users):
  
    if 'Days Active' in days_active.columns and 'NEW_USERS' in new_users.columns:

        correlation = days_active['Days Active'].corr(new_users['NEW_USERS'])
        correlation_df = pd.DataFrame({'Correlation': [correlation]})

    
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
        os.makedirs(output_dir, exist_ok=True)
        
     
        correlation_df.to_csv(os.path.join(output_dir, 'correlation_output.csv'), index=False)

       
        plt.figure(figsize=(10, 6))
        plt.scatter(days_active['Days Active'], new_users['NEW_USERS'], alpha=0.5)
        plt.xlabel('Days Active')
        plt.ylabel('New Users')
        plt.title(f'Correlation: {correlation}')
        plt.savefig(os.path.join(output_dir, 'correlation_scatter_plot.png'))
        plt.close()

        print("Correlation analysis complete. Data saved to 'output/correlation_output.csv' and scatter plot to 'output/correlation_scatter_plot.png'.")
    else:
        print("The required columns for correlation were not found in the datasets.")

if __name__ == "__main__":
    from load_data import load_csv

    
    days_active = load_csv('weekly_days_active.csv')
    new_users = load_csv('weekly_new_users.csv')
    
    correlation_analysis(days_active, new_users)
