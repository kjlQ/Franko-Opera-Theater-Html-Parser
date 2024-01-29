import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad requests
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None

# URL of the afisha page
afisha_url = "http://tickets.ft.org.ua/web/afisha"

# Fetch HTML content from the network
html_content = get_html_content(afisha_url)

if html_content:
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all elements with the class "for-info"
    for_info_elements = soup.find_all(class_="for-info")

    # Initialize a variable to count the number of tickets
    num_tickets = 0

    # Iterate through each "for-info" element
    for for_info_element in for_info_elements:
        # Find the link to the event page
        event_link = for_info_element.find('a', href=True)
        # Check if the element contains information about the "Конотопська відьма" event
        if event_link and "Конотопська відьма" in event_link.get_text().strip():
            num_tickets += 1

    print(f"Number of tickets for 'Конотопська відьма': {num_tickets}")
