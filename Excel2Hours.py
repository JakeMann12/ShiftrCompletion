from datetime import datetime, timedelta, time
import pandas as pd
from selenium import webdriver

def combine_date_and_time(t):
    if isinstance(t, time):
        return datetime.combine(datetime.today(), t)
    else:
        return None

def generate_selenium_string(row):
    def find_previous_date(day_name, weeks_ago):
        day_dict = {"Monday": 1,"Tuesday": 2,"Wednesday": 3,"Thursday": 4,"Friday": 5}
        adjusted_date = datetime.now() - timedelta(weeks=weeks_ago)
        target_day_num = day_dict[day_name]
        # Calculate the difference in days and adjust
        days_difference = (target_day_num - adjusted_date.isoweekday() + 7) % 7
        if days_difference == 0:
            days_difference = 7  # Ensure we move to the next week if it's the same day
        desired_date = adjusted_date + timedelta(days=days_difference)
        return desired_date

    date_format = "%m%d%Y"
    time_format = "%I%M"

    # Assuming clock-in and clock-out are already datetime.time objects or None
    clock_in = combine_date_and_time(row['Clock-in (24HR TIME)'])
    clock_out = combine_date_and_time(row['Clock-out (24HR time)'])
    if clock_in is None or clock_out is None:
        return None  # Skip rows with invalid time data

    am_pm_in = 'AM' if clock_in.hour < 12 else 'PM'
    am_pm_out = 'AM' if clock_out.hour < 12 else 'PM'
    designhub_or_colab = 'd' if row['DesignHub or Colab'].lower() == 'designhub' else 'c'

    day_of_week = row['Day of Week']
    date_two_weeks_ago = find_previous_date(day_of_week, 2).strftime(date_format)
    date_one_week_ago = find_previous_date(day_of_week, 1).strftime(date_format)
    formatted_clock_in = clock_in.strftime(time_format)
    formatted_clock_out = clock_out.strftime(time_format)

    selenium_string_two_weeks_ago = f"{date_two_weeks_ago}\t{formatted_clock_in}{am_pm_in}\t{date_two_weeks_ago}\t{formatted_clock_out}{am_pm_out}\t{designhub_or_colab}\t{row['Description']}"
    selenium_string_one_week_ago = f"{date_one_week_ago}\t{formatted_clock_in}{am_pm_in}\t{date_one_week_ago}\t{formatted_clock_out}{am_pm_out}\t{designhub_or_colab}\t{row['Description']}"

    return selenium_string_two_weeks_ago, selenium_string_one_week_ago

if __name__ == "__main__":
    # Load the Excel file
    file_path = 'Hours.xlsx'  # Replace with the correct path to your Excel file
    data = pd.read_excel(file_path)

    # Process each row to generate Selenium strings
    selenium_strings = [generate_selenium_string(row) for _, row in data.iterrows() if generate_selenium_string(row) is not None]

    # Display the first few generated strings for demonstration
    print(selenium_strings)
