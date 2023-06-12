import csv
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR, SA, SU

# Input Parameters
demo = input("Would you like to use demo data? (yes/no): ").lower()

if demo == "yes":
    queue_name = "<Queue_Name>"
    queue_id = "<Queue_ID>"
    channel_type = "VOICE"
    start_date = "2022-04-01"
    end_date = "2023-05-01"
    interval_input = "30mins"
    interval = 30
    open_time = 8
    close_time = 17
    min_volume = 60
    max_volume = 120
    min_handle_time = 3
    max_handle_time = 6
    low_percentage_handled = 0.6
    high_percentage_handled = 0.8
    working_days_input = [1, 2, 3, 4, 5]
else:
    print("Please enter the following parameters:")
    queue_name = input("Queue Name: ")
    queue_id = input("Queue ID: ")
    channel_type = input("Channel Type (CHAT or VOICE): ").upper()
    while channel_type not in ['CHAT', 'VOICE']:
        print("Invalid channel type. Please enter either CHAT or VOICE.")
        channel_type = input("Channel Type (CHAT or VOICE): ").upper()

    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")

    while True:
        interval_input = input("Interval (15mins, 30mins, or daily for long-term forecast): ")
        if interval_input.lower() in ['15mins', '30mins']:
            interval = int(interval_input[:-4])
            break
        elif interval_input.lower() == 'daily':
            interval = 1440
            break
        else:
            print("Invalid interval. Please enter either 15mins, 30mins or daily.")

    open_time = int(input("Opening time (24-hour format): "))
    close_time = int(input("Closing time (24-hour format): "))
    min_volume = int(input("Minimum incoming contact volume: "))
    max_volume = int(input("Maximum incoming contact volume: "))
    while min_volume > max_volume:
        print("Minimum volume cannot be greater than maximum volume.")
        min_volume = int(input("Minimum incoming contact volume: "))
        max_volume = int(input("Maximum incoming contact volume: "))

    min_handle_time = int(input("Minimum average handle time in minutes: "))
    max_handle_time = int(input("Maximum average handle time in minutes: "))
    while min_handle_time > max_handle_time:
        print("Minimum handle time cannot be greater than maximum handle time.")
        min_handle_time = int(input("Minimum average handle time in minutes: "))
        max_handle_time = int(input("Maximum average handle time in minutes: "))

    low_percentage_handled = float(input("Low Calls Handled Percentage (e.g., enter 60 for 60%): ")) / 100
    high_percentage_handled = float(input("High Calls Handled Percentage (e.g., enter 90 for 90%): ")) / 100
    while low_percentage_handled > high_percentage_handled:
        print("Low percentage handled cannot be greater than high percentage handled.")
        low_percentage_handled = float(input("Low Calls Handled Percentage (e.g., enter 60 for 60%): ")) / 100
        high_percentage_handled = float(input("High Calls Handled Percentage (e.g., enter 90 for 90%): ")) / 100

    print("Input the days when the contact center is open:")
    print("1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday, 6 for Saturday, 7 for Sunday")
    working_days_input = list(map(int, input("Enter the numbers separated by comma: ").split(',')))

# Generate CSV
working_days = []
for day in working_days_input:
    if day == 1:
        working_days.append(MO)
    elif day == 2:
        working_days.append(TU)
    elif day == 3:
        working_days.append(WE)
    elif day == 4:
        working_days.append(TH)
    elif day == 5:
        working_days.append(FR)
    elif day == 6:
        working_days.append(SA)
    elif day == 7:
        working_days.append(SU)

dates = list(rrule(DAILY, dtstart=datetime.strptime(start_date, "%Y-%m-%d"), until=datetime.strptime(end_date, "%Y-%m-%d"), byweekday=working_days))

output = []
for date in dates:
    if interval_input.lower() == 'daily':
        contact_volume = np.random.randint(min_volume, max_volume + 1)
        handle_time = round(np.random.uniform(min_handle_time, max_handle_time) * 60)
        percentage_handled = np.random.uniform(low_percentage_handled, high_percentage_handled)
        calls_handled = int(contact_volume * percentage_handled)
        timestamp = datetime(date.year, date.month, date.day, 0, 0, 0)
        output.append([queue_name, queue_id, channel_type, timestamp.isoformat()+'Z', interval_input.lower(), contact_volume, handle_time, calls_handled])
    else:
        start_time = datetime(date.year, date.month, date.day, open_time, 0, 0)
        end_time = datetime(date.year, date.month, date.day, close_time, 0, 0)
        while start_time < end_time:
            contact_volume = np.random.randint(min_volume, max_volume + 1)
            handle_time = round(np.random.uniform(min_handle_time, max_handle_time) * 60)
            percentage_handled = np.random.uniform(low_percentage_handled, high_percentage_handled)
            calls_handled = int(contact_volume * percentage_handled)
            timestamp = start_time
            output.append([queue_name, queue_id, channel_type, timestamp.isoformat()+'Z', interval_input.lower(), contact_volume, handle_time, calls_handled])
            start_time += timedelta(minutes=interval)

df = pd.DataFrame(output, columns=['QueueName', 'QueueId', 'ChannelType', 'TimeStamp', 'IntervalDuration', 'IncomingContactVolume', 'AverageHandleTime', 'ContactsHandled'])
df.to_csv('output.csv', index=False)
print("\nCSV file has been generated with the filename 'output.csv'.")
