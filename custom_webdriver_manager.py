from selenium import webdriver
from pathlib import Path
import json

# Function to load cookies from a specified username in the single data file
def load_cookies(driver, username_insta):
    data_file = Path('./cookies_data.txt')

    if data_file.exists():
        with data_file.open('r') as file:
            # Read each line as a JSON object
            for line in file:
                data = json.loads(line.strip())
                # Find the entry matching the specified username
                if data.get("username") == username_insta:
                    for cookie in data.get("cookies", []):
                        driver.add_cookie(cookie)
                    print(f"Cookies loaded for username: {username_insta}")
                    return
        print(f"No cookies found for username: {username_insta}")
    else:
        print("Cookies data file does not exist.")

# Initialize the browser
driver = webdriver.Chrome()

# Navigate to the target website
driver.get("https://www.instagram.com/")  # Replace "DOMAIN" with the actual domain, e.g., "https://www.instagram.com/"

# Load cookies for the specified username
username_insta = "gabriel.haefli"  # Change this to the desired username
load_cookies(driver, username_insta)

# Refresh the page to apply the cookies
driver.refresh()

# Continue with your browsing actions
# ...
while True:
    x = input("QUIT? ")
    if x.upper() == "JA":
        driver.quit()
        break
