# Import the required libraries
import requests

# Define the phone number to trace
phone_number = "+1234567890"

# Define the URL for the API endpoint
url = f"https://api.example.com/trace?phone={phone_number}"

# Send a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the location information from the response
    location = response.json()["location"]
    print(f"The location of the phone number {phone_number} is: {location}")
else:
    print("Failed to retrieve location information")
