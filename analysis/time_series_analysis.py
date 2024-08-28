import pandas as pd
import matplotlib.pyplot as plt
import os

def calculate_metrics(new_users, days_since_last_use):

    transparency_score_increase = new_users['NEW_USERS'].pct_change().mean() * 100

    shipping_time_reduction = days_since_last_use['Days since last use'].pct_change().mean() * 100

 
    shipping_time_reduction = -shipping_time_reduction

    return transparency_score_increase, shipping_time_reduction

def time_series_analysis(new_users, days_active, days_since_last_use):
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)

   
    new_users['WEEK'] = pd.to_datetime(new_users['WEEK'])
    days_active['CREATION_DATE'] = pd.to_datetime(days_active['CREATION_DATE'])
    days_since_last_use['CREATION_DATE'] = pd.to_datetime(days_since_last_use['CREATION_DATE'])

 
    common_start = max(new_users['WEEK'].min(), days_active['CREATION_DATE'].min(), days_since_last_use['CREATION_DATE'].min())
    common_end = min(new_users['WEEK'].max(), days_active['CREATION_DATE'].max(), days_since_last_use['CREATION_DATE'].max())

   
    new_users_filtered = new_users[(new_users['WEEK'] >= common_start) & (new_users['WEEK'] <= common_end)]
    days_active_filtered = days_active[(days_active['CREATION_DATE'] >= common_start) & (days_active['CREATION_DATE'] <= common_end)]
    days_since_last_use_filtered = days_since_last_use[(days_since_last_use['CREATION_DATE'] >= common_start) & (days_since_last_use['CREATION_DATE'] <= common_end)]

    
    transparency_score_increase, shipping_time_reduction = calculate_metrics(new_users_filtered, days_since_last_use_filtered)

    print(f"Shipping Time Reduction: {shipping_time_reduction:.2f}%")
    print(f"Transparency Score Increase: {transparency_score_increase:.2f}%")

    fig, ax1 = plt.subplots(figsize=(14, 7))

    ax1.plot(new_users_filtered['WEEK'], new_users_filtered['NEW_USERS'], label='New Users', color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('New Users', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(days_active_filtered['CREATION_DATE'], days_active_filtered['Days Active'], label='Days Active', color='green')
    ax2.set_ylabel('Days Active', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))
    ax3.plot(days_since_last_use_filtered['CREATION_DATE'], days_since_last_use_filtered['Days since last use'], label='Days Since Last Use', color='red')
    ax3.set_ylabel('Days Since Last Use', color='red')
    ax3.tick_params(axis='y', labelcolor='red')

    plt.annotate(f'Shipping Time Reduction: {shipping_time_reduction:.2f}%', xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10, color='red', backgroundcolor='white')
    plt.annotate(f'Transparency Score Increase: {transparency_score_increase:.2f}%', xy=(0.05, 0.90), xycoords='axes fraction', fontsize=10, color='blue', backgroundcolor='white')

    ax1.xaxis.set_major_locator(plt.MaxNLocator(10))
    fig.autofmt_xdate()

    plt.title('User Engagement and Transparency Over Time')
    fig.tight_layout()

    # Save the plot
    plt.savefig(os.path.join(output_dir, 'transparency_engagement_plot_corrected.png'))
    plt.close()

    print(f"Time series analysis complete. Data and plot saved to {output_dir}")

if __name__ == "__main__":
    # Define the data directory
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')

    # Load the datasets
    new_users = pd.read_csv(os.path.join(data_dir, 'weekly_new_users.csv'))
    days_active = pd.read_csv(os.path.join(data_dir, 'weekly_days_active.csv'))
    days_since_last_use = pd.read_csv(os.path.join(data_dir, 'weekly_days_since_last_use.csv'))

    # Perform the analysis
    time_series_analysis(new_users, days_active, days_since_last_use)
