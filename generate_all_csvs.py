from scripts.generate_program_flipside_labels import generate_program_flipside_labels
from scripts.generate_program_solana_fm_labels import generate_program_solana_fm_labels
from scripts.generate_weekly_days_active import generate_weekly_days_active
from scripts.generate_weekly_days_since_last_use import generate_weekly_days_since_last_use
from scripts.generate_weekly_new_program import generate_weekly_new_program
from scripts.generate_weekly_new_users import generate_weekly_new_users
from scripts.generate_weekly_program import generate_weekly_program
from scripts.generate_weekly_users import generate_weekly_users
from scripts.generate_weekly_users_last_use import generate_weekly_users_last_use

def generate_all_csvs():
    generate_program_flipside_labels()
    generate_program_solana_fm_labels()
    generate_weekly_days_active()
    generate_weekly_days_since_last_use()
    generate_weekly_new_program()
    generate_weekly_new_users()
    generate_weekly_program()
    generate_weekly_users()
    generate_weekly_users_last_use()

if __name__ == "__main__":
    generate_all_csvs()
