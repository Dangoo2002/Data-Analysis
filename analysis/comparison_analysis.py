import pandas as pd
import matplotlib.pyplot as plt
import os

def load_csv(filename):
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
    file_path = os.path.join(data_dir, filename)
    return pd.read_csv(file_path)

def analyze_data(program_data, days_since_last_use):
    # Convert date columns to datetime
    program_data['WEEK'] = pd.to_datetime(program_data['WEEK'])
    days_since_last_use['CREATION_DATE'] = pd.to_datetime(days_since_last_use['CREATION_DATE'])
    
    # Sort the dataframes by date
    program_data = program_data.sort_values('WEEK')
    days_since_last_use = days_since_last_use.sort_values('CREATION_DATE')
    
    # Calculate percentage change in unique programs
    program_data['UNIQUE_PROGRAMS_PCT_CHANGE'] = program_data['UNIQUE_PROGRAMS'].pct_change() * 100
    
    # Create the plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    # Plot Unique Programs
    ax1.plot(program_data['WEEK'], program_data['UNIQUE_PROGRAMS'], color='blue')
    ax1.set_ylabel('Unique Programs', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    
    # Plot Days since last use
    ax2.plot(days_since_last_use['CREATION_DATE'], days_since_last_use['Days since last use'], color='orange')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Days since last use', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    
    plt.title('Unique Programs and Days Since Last Use Over Time')
    fig.tight_layout()
    
    # Save the plot
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'data_analysis_plot.png'))
    plt.close(fig)
    
    # Calculate statistics
    program_stats = {
        'max_unique_programs': program_data['UNIQUE_PROGRAMS'].max(),
        'min_unique_programs': program_data['UNIQUE_PROGRAMS'].min(),
        'avg_unique_programs': program_data['UNIQUE_PROGRAMS'].mean(),
        'total_reduction_percentage': ((program_data['UNIQUE_PROGRAMS'].iloc[0] - program_data['UNIQUE_PROGRAMS'].iloc[-1]) / program_data['UNIQUE_PROGRAMS'].iloc[0]) * 100,
        'max_reduction_percentage': program_data['UNIQUE_PROGRAMS_PCT_CHANGE'].min(),
        'max_reduction_week': program_data.loc[program_data['UNIQUE_PROGRAMS_PCT_CHANGE'].idxmin(), 'WEEK']
    }
    
    days_stats = {
        'max_days_since_last_use': days_since_last_use['Days since last use'].max(),
        'min_days_since_last_use': days_since_last_use['Days since last use'].min(),
        'avg_days_since_last_use': days_since_last_use['Days since last use'].mean()
    }
    
    return program_stats, days_stats

if __name__ == "__main__":
    program_data = load_csv('weekly_program.csv')
    days_since_last_use = load_csv('weekly_days_since_last_use.csv')
    program_stats, days_stats = analyze_data(program_data, days_since_last_use)
    
    print("Data analysis complete. Results:")
    print("\nUnique Programs Statistics:")
    print(f"Maximum unique programs: {program_stats['max_unique_programs']}")
    print(f"Minimum unique programs: {program_stats['min_unique_programs']}")
    print(f"Average unique programs: {program_stats['avg_unique_programs']:.2f}")
    print(f"Total reduction in unique programs: {program_stats['total_reduction_percentage']:.2f}%")
    print(f"Maximum week-over-week reduction: {abs(program_stats['max_reduction_percentage']):.2f}%")
    print(f"Week of maximum reduction: {program_stats['max_reduction_week']}")
    print("\nDays Since Last Use Statistics:")
    print(f"Maximum days since last use: {days_stats['max_days_since_last_use']:.2f}")
    print(f"Minimum days since last use: {days_stats['min_days_since_last_use']:.2f}")
    print(f"Average days since last use: {days_stats['avg_days_since_last_use']:.2f}")
    print("\nPlot saved to 'output/data_analysis_plot.png'.")