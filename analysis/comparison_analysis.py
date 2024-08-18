import pandas as pd
import matplotlib.pyplot as plt
import os

def comparison_analysis(program_data, days_since_last_use):

    program_data['WEEK'] = pd.to_datetime(program_data['WEEK'])
    days_since_last_use['CREATION_DATE'] = pd.to_datetime(days_since_last_use['CREATION_DATE'])

    comparison_df = pd.merge(
        program_data[['WEEK', 'UNIQUE_PROGRAMS']],
        days_since_last_use[['CREATION_DATE', 'Days since last use']],
        left_on='WEEK', right_on='CREATION_DATE',
        how='outer' 
    )

   
    comparison_df.rename(columns={
        'WEEK': 'Week',
        'UNIQUE_PROGRAMS': 'Program Count',
        'Days since last use': 'Days Since Last Use'
    }, inplace=True)


    comparison_df.sort_values(by='Week', inplace=True)

    comparison_df['Program Count'].fillna(0, inplace=True)
    comparison_df['Days Since Last Use'].fillna(0, inplace=True)
 
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    comparison_df.to_csv(os.path.join(output_dir, 'comparison_data.csv'), index=False)
    
    # Create the comparison plot
    plt.figure(figsize=(12, 6))
    plt.plot(comparison_df['Week'], comparison_df['Program Count'], label='Program Count')
    plt.plot(comparison_df['Week'], comparison_df['Days Since Last Use'], label='Days Since Last Use')
    plt.xlabel('Week')
    plt.ylabel('Count')
    plt.title('Program Count and Days Since Last Use Over Time')
    plt.legend()
    
    # Save the plot as a PNG file
    plt.savefig(os.path.join(output_dir, 'comparison_plot.png'))
    plt.close()  

    print("Comparison analysis complete. Data and plot saved to 'output/comparison_data.csv' and 'output/comparison_plot.png'.")

if __name__ == "__main__":
    from load_data import load_csv

   
    program_data = load_csv('weekly_program.csv')
    days_since_last_use = load_csv('weekly_days_since_last_use.csv')
    
    comparison_analysis(program_data, days_since_last_use)
