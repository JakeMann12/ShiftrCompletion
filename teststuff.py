import pandas as pd

hours = pd.read_excel('Hours.xlsx')

print(hours)

from datetime import datetime, timedelta
import pandas as pd

# Get the current date
current_date = datetime.now()

# Subtract two weeks
two_weeks_ago = current_date - timedelta(weeks=3)

# Create a dictionary to map day names to corresponding dates
day_mapping = {
    "Monday": (two_weeks_ago - timedelta(days=(two_weeks_ago.weekday() - 0) % 7)).strftime("%m/%d/%Y"),
    "Tuesday": (two_weeks_ago - timedelta(days=(two_weeks_ago.weekday() - 1) % 7)).strftime("%m/%d/%Y"),
    "Wednesday": (two_weeks_ago - timedelta(days=(two_weeks_ago.weekday() - 2) % 7)).strftime("%m/%d/%Y"),
    "Thursday": (two_weeks_ago - timedelta(days=(two_weeks_ago.weekday() - 3) % 7)).strftime("%m/%d/%Y"),
    "Friday": (two_weeks_ago - timedelta(days=(two_weeks_ago.weekday() - 4) % 7)).strftime("%m/%d/%Y"),
    "Saturday": (two_weeks_ago - timedelta(days=(two_weeks_ago.weekday() - 5) % 7)).strftime("%m/%d/%Y"),
    "Sunday": (two_weeks_ago - timedelta(days=(two_weeks_ago.weekday() - 6) % 7)).strftime("%m/%d/%Y"),
}

# Sample Excel data with days of the week
excel_data = {"DayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

# Create a DataFrame from the Excel data
df = pd.DataFrame(excel_data)

# Map the day names to corresponding dates
df["CorrespondingDate"] = df["DayOfWeek"].map(day_mapping)

# Display the result
print(df)

from datetime import datetime, timedelta

def find_recent_day(day_name, weeks_ago):
    day_dict = {"Monday": 1,"Tuesday": 2,"Wednesday": 3,"Thursday": 4,"Friday": 5}
    adjusted_date = datetime.now() - timedelta(weeks=weeks_ago)
    target_day_num = day_dict[day_name]
    # Calculate the difference in days and adjust
    days_difference = (target_day_num - adjusted_date.isoweekday() + 7) % 7
    if days_difference == 0:
        days_difference = 7  # Ensure we move to the next week if it's the same day
    desired_date = adjusted_date + timedelta(days=days_difference)

    return desired_date

# Example usage
today = datetime.now() + timedelta(days=-4)  # Adjust the current date as necessary
day = "Wednesday"
weeks_ago = 2
closest_day = find_recent_day(day, weeks_ago)
print("Next closest", day, ":", closest_day.strftime("%Y-%m-%d"))