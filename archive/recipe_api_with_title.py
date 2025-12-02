
import requests # Must be the python package
import os # To manoeuver around files
from dotenv import load_dotenv # To loads files from .env
from urllib.parse import quote # To handle user input for URL

load_dotenv() # Actually loading files from .env

API_NINJAS_KEY = os.getenv("API_NINJAS_KEY") # Creating the variable from the other file
RECIPE_SOURCE_URL = os.getenv("RECIPE_SOURCE_URL") # Creating the variable from the other file

# And then it looks like instead of printing it, you do a safety check...
if not API_NINJAS_KEY:
    raise RuntimeError(
        "API_NINJAS_KEY not found in .env. "
        "Did you create .env from .env.example and add your key?"
    )
# Maybe a little print.
print(f"Key loaded successfully (first 10 chars): {API_NINJAS_KEY[:10]}...")


# TODO: Refactor these two checks so they're not separate?
if not RECIPE_SOURCE_URL:
    raise RuntimeError(
        "RECIPE_SOURCE_URL not found in .env. "
    )
print(f"Source URL loaded successfully: {RECIPE_SOURCE_URL}")

# Preparing the header for the API call
headers = {
    "X-Api-Key": API_NINJAS_KEY
}

# Gonna need a user input, at least for testing
user_input = "Lentil Soup" # TODO Eventually must be hooked to the chat with the agent.
print(f"{user_input} - original") 

# URL-encode it (spaces → %20)
encoded_query = quote(user_input).lower()
print(f"{encoded_query} - converted to URL-friendly chars")

# Build the 'title' parameter for the API call
title_API = (f"?title={encoded_query}")

# Just to check
print(title_API)

# Building out the URL
url = f"{RECIPE_SOURCE_URL}{title_API}"
print(url)

# Make a GET request to an API endpoint

response = requests.get(
    url, 
    headers = headers,
    timeout=10 # Good practice
)

# Handling the response
if response.status_code == 200:
    data = response.json()
    print("It worked!")
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(f"Response: {response.text}") # Shows error details, must be inbuilt?



