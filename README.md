SMS Bomb Sender

This Python script allows you to send multiple SMS messages to one or more mobile numbers using an external API endpoint. It features a hacking-themed interface with ASCII art and loading animations.
Features

    Send SMS to a single number with configurable attempts.
    Send SMS to multiple numbers simultaneously with configurable attempts.
    Hacking-themed user interface with ASCII art and dynamic loading animations.

Prerequisites

    Python 3.x
    Required Python packages (requests, colorama, keyboard)

Installation

    Clone the repository:

    bash

git clone https://github.com/dularawe/SMS_Bomb.git
cd sms-bomb-sender

Install dependencies:

bash

    pip install -r requirements.txt

Usage

    Navigate to the project directory.

    Run the script:

    bash

    python sms_bomb_sender.py

    Choose an option from the menu:
        Option 1: Send SMS to a single number.
            Enter the mobile number and the number of attempts.
        Option 2: Send SMS to multiple numbers.
            Enter multiple phone numbers separated by commas and the number of attempts.
        Press Esc to exit the program.

Example
Sending SMS to a Single Number

bash

$ python sms_bomb_sender.py

Welcome to the SMS Bomb Sender!

Choose an option:
1. Send SMS to a single number
2. Send SMS to multiple numbers
Esc. Exit program

Enter your choice (1, 2, or Esc): 1

Enter the mobile number to send SMS: 1234567890
How many times would you like to attempt to send SMS to 1234567890? 3

Attempting to send SMS to 1234567890...
Hacking... █ (Attempt 1)  [Success]
Hacking... ▒ (Attempt 2)  [Failed]
Hacking... ▒ (Attempt 3)  [Success]

All attempts completed.

Sending SMS to Multiple Numbers

bash

$ python sms_bomb_sender.py

Welcome to the SMS Bomb Sender!

Choose an option:
1. Send SMS to a single number
2. Send SMS to multiple numbers
Esc. Exit program

Enter your choice (1, 2, or Esc): 2

Enter phone numbers separated by commas: 1234567890, 9876543210
How many times would you like to attempt to send SMS to each number? 2

Attempting to send SMS to 1234567890...
Hacking... █ (Attempt 1)  [Success]
Hacking... ▒ (Attempt 2)  [Failed]

Attempting to send SMS to 9876543210...
Hacking... █ (Attempt 1)  [Success]
Hacking... ▒ (Attempt 2)  [Success]

All attempts completed.
