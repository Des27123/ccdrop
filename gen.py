import asyncio
import random
import requests
from faker import Faker
from telegram import Bot

cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    # Add more cities here
]

states = [
    "New York",
    "California",
    "Illinois",
    # Add corresponding states here
]

def generate_bin():
    bin_number = random.randint(400000, 499999)
    bin_number_str = str(bin_number)
    credit_card_number = f"{bin_number_str}{''.join(random.choice('0123456789') for _ in range(10))}"
    return bin_number_str, credit_card_number

def get_bin_info(bin_number):
    url = f"https://lookup.binlist.net/{bin_number}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            bin_info = response.json()
            if bin_info:
                fake = Faker()
                city = random.choice(cities)
                state = states[cities.index(city)]
                message = f"*+++++++++++++++[-] Card Information [-]+++++++++++++++*\n\n"
                message += f"[+] Cardholder Name: {fake.name()}\n"
                message += f"[+] Street: {fake.street_address()}\n"
                message += f"[+] City/Town: {city}\n"
                message += f"[+] State/Province/Region: {state}\n"
                message += f"[+] Zip/Postal Code: {fake.zipcode()}\n"
                message += f"[+] Phone Number: {fake.phone_number()}\n"
                message += f"+----------------------------------------+\n"
                message += f"[+] BIN Information [+]\n"
                message += f"[+] BIN: {bin_number}\n"
                message += f"[+] Card Type: {bin_info.get('type', 'N/A')}\n"
                message += f"[+] Brand: {bin_info.get('brand', 'N/A')}\n"
                message += f"[+] Bank Name: {bin_info.get('bank', {}).get('name', 'N/A')}\n"
                message += f"[+] Credit Card Number: {bin_number + ''.join(random.choice('0123456789') for _ in range(10))}\n"
                message += f"[+] Expiration Date: {fake.credit_card_expire()}\n"
                message += f"[+] CVV: {random.randint(100, 999)}\n"
                message += f"+----------------------------------------+\n"
                message += f"[+] Additional Information [+]\n"
                message += f"[+] City/Town: {city}\n"
                message += f"[+] State/Province/Region: {state}\n"
                message += f"[+] Birthdate: {fake.date_of_birth(minimum_age=18, maximum_age=90)}\n"
                message += f"[+] Password: {fake.password(length=10)}\n"
                message += f"[+] Username: {fake.user_name()}\n"
                message += f"[+] IP Address: {fake.ipv4()}\n"
                message += f"[+] MAC Address: {fake.mac_address()}\n"
                message += f"[+] User Agent: {fake.user_agent()}\n"
                message += f"+--Fullz By @Adrain27----+\n"
                return message
            else:
                return "Invalid BIN Input!!"
        else:
            return "Unable to retrieve BIN information"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

async def send_message_to_telegram(message, token, chat_id):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=message)

async def main():
    bot_token = "Add_bot_token_here"
    channel_username = "@Username"  # e.g., "@binstesthere"
    
    # Display custom logo or text when the script is run
    print("*+++++++++++++++ Welcome to the BIN Sender Script! +++++++++++++++*")
    
    while True:
        bin_number, credit_card_number = generate_bin()
        bin_info = get_bin_info(bin_number)
        
        # Show that the bin is sent successfully
        print(f"BIN {bin_number} sent successfully!")
        
        await send_message_to_telegram(bin_info, bot_token, channel_username)
        await asyncio.sleep(60)  # Wait for 60 seconds before sending the next message

if __name__ == "__main__":
    asyncio.run(main())
