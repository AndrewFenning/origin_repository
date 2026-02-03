import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
} #needed help from gen AI to figure out that I needed to fake a user header kind of thing  to bypass the wikipedia bot redirects.

response = requests.get(url, headers = headers)
# response.raise_for_status() #checking if request was successful

parsed_text = BeautifulSoup(response.text, 'html.parser')

page_title = parsed_text.title.string

print(f"Page Title: {page_title}")

content_div = parsed_text.find('div', id='mw-content-text')

if content_div:
    paragraphs = content_div.find_all('p')

    found_paragraph = None
    for p in paragraphs:
        text = p.get_text().strip()
        if len(text) >= 50:
            found_paragraph = text
            break

    if found_paragraph:
        print("First valid paragraph (>= 50 chars):")
        print(found_paragraph)
    else:
        print("No paragraph meeting the length requirement was found.")
else:
    print("Could not find the content div. The structure of the page might have changed.")