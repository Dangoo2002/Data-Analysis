import os
from analysis.correlation_analysis import correlation_analysis
from analysis.time_series_analysis import time_series_analysis
from analysis.comparison_analysis import comparison_analysis
from analysis.distribution_analysis import distribution_analysis
from analysis.load_data import load_data
from analysis.clean_data import clean_data

def main():
    # Load and clean data
    data = load_data()
    cleaned_data = clean_data(data)

    
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Perform analyses and save outputs
    correlation_analysis(cleaned_data['days_active'], cleaned_data['new_users'])
    time_series_analysis(cleaned_data['new_users'])
    comparison_analysis(cleaned_data['program_data'], cleaned_data['days_since_last_use'])
    distribution_analysis(cleaned_data['users_last_use'])

    print("All analyses completed successfully.")

if __name__ == "__main__":
    main()

    
    if os.path.exists('__pycache__'):
        import shutil
        shutil.rmtree('__pycache__')
