import pandas as pd
import matplotlib.pyplot as plt
import os

def distribution_analysis():
    # Load data
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
    weekly_program = pd.read_csv(os.path.join(data_dir, 'weekly_program.csv'))
    weekly_new_program = pd.read_csv(os.path.join(data_dir, 'weekly_new_program.csv'))


    weekly_program['WEEK'] = pd.to_datetime(weekly_program['WEEK'])
    weekly_new_program['WEEK'] = pd.to_datetime(weekly_new_program['WEEK'])

    blockchain_adoption_date = '2021-06-01'
    before_adoption = weekly_program[weekly_program['WEEK'] < blockchain_adoption_date]
    after_adoption = weekly_program[weekly_program['WEEK'] >= blockchain_adoption_date]

    mean_unique_programs_before = before_adoption['UNIQUE_PROGRAMS'].mean()
    mean_unique_programs_after = after_adoption['UNIQUE_PROGRAMS'].mean()


    percent_change = ((mean_unique_programs_after - mean_unique_programs_before) / mean_unique_programs_before) * 100

    mean_new_programs_before = weekly_new_program[weekly_new_program['WEEK'] < blockchain_adoption_date]['New Programs'].mean()
    mean_new_programs_after = weekly_new_program[weekly_new_program['WEEK'] >= blockchain_adoption_date]['New Programs'].mean()

    categories = ['Before Blockchain', 'After Blockchain']
    unique_programs_means = [mean_unique_programs_before, mean_unique_programs_after]
    new_programs_means = [mean_new_programs_before, mean_new_programs_after]

    fig, ax1 = plt.subplots(figsize=(12, 7))
    bars = ax1.bar(categories, unique_programs_means, color='b', alpha=0.6, label='Mean Unique Programs')
    ax1.set_xlabel('Blockchain Adoption Status')
    ax1.set_ylabel('Mean Unique Programs', color='b')
    ax1.tick_params(axis='y', labelcolor='b')


    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.0f}',
                 ha='center', va='bottom')

    ax2 = ax1.twinx()
    ax2.plot(categories, new_programs_means, color='r', marker='o', label='Mean New Programs Introduced')
    ax2.set_ylabel('Mean New Programs Introduced', color='r')
    ax2.tick_params(axis='y', labelcolor='r')


    ax1.annotate(f'{percent_change:.1f}% Change', 
                 xy=(1, mean_unique_programs_after), 
                 xytext=(1.2, (mean_unique_programs_before + mean_unique_programs_after) / 2),
                 arrowprops=dict(facecolor='red', shrink=0.05),
                 fontsize=12, color='red',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", lw=1))

    plt.title('Changes in Unique Programs and New Program Introductions\nBefore and After Blockchain Adoption')
    fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)

    fig.tight_layout()
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'efficiency_improvement_plot.png'), bbox_inches='tight')
    plt.close()

    print(f"Plot saved to {os.path.join(output_dir, 'efficiency_improvement_plot.png')}")
    print(f"Percentage change in Mean Unique Programs: {percent_change:.1f}%")

if __name__ == "__main__":
    distribution_analysis()