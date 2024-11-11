# main.py

import datetime
import bday_messages

# Get today's date
today = datetime.date.today()

# Set your next birthday date (replace with your actual birthday)
next_birthday = datetime.date(today.year, 12, 25)  # Example: December 25

# Check if birthday has already passed this year
if next_birthday < today:
    next_birthday = datetime.date(today.year + 1, 12, 25)

# Calculate the number of days until the next birthday
days_away = (next_birthday - today).days

# Display the message
if days_away == 0:
    print(bday_messages.random_message)
else:
    print(f"My next birthday is {days_away} days away!")
