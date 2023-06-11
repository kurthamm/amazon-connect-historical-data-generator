
Amazon Connect Historical Data Generator

This Python script generates a CSV file with randomized historical data for Amazon Connect's forecasting feature. The generated data includes the queue name, queue ID, channel type, timestamp, interval duration, incoming contact volume, average handle time, and the number of contacts handled.

Table of Contents

Installation
Usage
Contributing
License
Installation

Clone the repository to your local machine:

git clone https://github.com/yourusername/amazon-connect-historical-data-generator.git

Navigate to the project directory:

cd amazon-connect-historical-data-generator

Usage

Run the script and follow the prompts to input the necessary parameters. You can also choose to use demo data.

python historical_data_generator.py

Input Parameters

Queue Name: The name of the Amazon Connect queue.
Queue ID: The ID of the Amazon Connect queue.
Channel Type: The type of channel (CHAT or VOICE).
Start date: The start date of the historical data (YYYY-MM-DD).
End date: The end date of the historical data (YYYY-MM-DD).
Interval: The interval for the data (15mins, 30mins, or daily for long-term forecast).
Opening time: The opening time of the contact center (24-hour format).
Closing time: The closing time of the contact center (24-hour format).
Minimum incoming contact volume: The minimum number of incoming contacts.
Maximum incoming contact volume: The maximum number of incoming contacts.
Minimum average handle time: The minimum average handle time in minutes.
Maximum average handle time: The maximum average handle time in minutes.
Low Calls Handled Percentage: The low percentage of calls handled (e.g., enter 60 for 60%).
High Calls Handled Percentage: The high percentage of calls handled (e.g., enter 90 for 90%).
Working Days: The days when the contact center is open (1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday, 6 for Saturday, 7 for Sunday).
Output

The script generates a CSV file named 'output.csv' with the randomized historical data.

Contributing

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
License

Distributed under the MIT License. See LICENSE for more information.

Contact

Your Name - your_email@example.com

Project Link: https://github.com/yourusername/amazon-connect-historical-data-generator
