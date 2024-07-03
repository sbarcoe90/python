import requests
from bs4 import BeautifulSoup

url = 'https://www.adverts.ie/'

# Make a GET request to the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find elements you want to scrape by inspecting the webpage's HTML