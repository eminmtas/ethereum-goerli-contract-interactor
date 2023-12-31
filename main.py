import config
import datetime
from web3 import Web3
from web3.exceptions import InvalidAddress

# Global Variables
try:
    w3 = Web3(Web3.WebsocketProvider(config.infura_websocket))
    contract_instance = w3.eth.contract(address=config.contract_address, abi=config.abi)
except AttributeError:
    print("Contract address or ABI not found in config.")
    exit(1)

# Convert timestamp and calculate the difference from the current time
def convert_timestamp_to_date(timestamp: int) -> str:

    # Convert timestamp to a datetime object
    timestamp_date = datetime.datetime.fromtimestamp(timestamp)

    # Get the current time
    now = datetime.datetime.now()

    # Calculate the difference between the timestamp and the current time
    diff = timestamp_date - now

    # Calculate the difference in days
    days = diff.days

    # Calculate the difference in months, days, hours and minutes
    months, remaining_days, hours, minutes = days // 30, days % 30, diff.seconds // 3600, (diff.seconds // 60) % 60

    # Format the results and return
    result = "There are " + str(months) + " months " + str(remaining_days) + " days " + str(hours) + " hours and " + str(minutes) + " minutes left until the license expires."
    return result

# Get token IDs
def get_token_ids(address: str) -> list:

    return contract_instance.functions.printLicenseBalances(address).call()

# Get token details
def get_token_details(token_ids: list) -> list:

    token_details = []
    for token_id in token_ids:
        expiry_date = convert_timestamp_to_date(contract_instance.functions.licenseExpiry(token_id).call())
        token_details.append((token_id, expiry_date))
    return token_details

def main():

    # Menu
    while True:
        print("Menu:")
        print("1. Enter address")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            temp_address = str(input("Enter address: "))

            # Check if the address is valid
            if w3.is_address(temp_address) == True:
                tokenIds = get_token_ids(temp_address)
                token_details = get_token_details(tokenIds)
                if token_details:
                    token_with_longest_time = max(token_details, key=lambda x: x[1])
                    print("------------------------------------")
                    print(f"The ID of the License that has the most remaining time is {token_with_longest_time[0]} \n{token_with_longest_time[1]}")
                    print("------------------------------------")
                else:
                    print("No tokens found.\n")
            else:
                print("\nINVALID ETHEREUM ADDRESS. TRY ANOTHER ADDRESS\n")
            
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("------------------------------------")
            print("Invalid choice. Please enter 1 or 2.\n")



if __name__ == "__main__":
    main()

