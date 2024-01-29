import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None

afisha_url = "http://tickets.ft.org.ua/web/afisha"

html_content = get_html_content(afisha_url)

if html_content:
    soup = BeautifulSoup(html_content, 'html.parser')
    for_info_elements = soup.find_all(class_="for-info")
    num_tickets = 0
    for for_info_element in for_info_elements:
        event_link = for_info_element.find('a', href=True)
        if event_link and "Конотопська відьма" in event_link.get_text().strip():
            num_tickets += 1

    print(f"Number of tickets for 'Конотопська відьма': {num_tickets}")
