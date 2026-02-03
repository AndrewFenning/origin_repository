import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


response = requests.get(url, headers=headers)
response.raise_for_status()

# parse
soup = BeautifulSoup(response.text, 'html.parser')

# main content area
content_div = soup.find('div', id='mw-content-text')

if content_div:
    # Extract all <h2> tags inside the content div
    h2_tags = content_div.find_all('h2')

    valid_headings = []
    excluded_words = ["References", "External links", "See also", "Notes"]

    for h2 in h2_tags:
        # Get text and clean it
        text = h2.get_text()

        # Remove "[edit]" text if present
        text = text.replace("[edit]", "").strip()

        # Check if the heading contains any forbidden words
        # tracking if we should skip this heading
        is_excluded = False
        for word in excluded_words:
            if word in text:
                is_excluded = True
                break

        # Only add to list if not excluded and not empty
        if not is_excluded and text:
            valid_headings.append(text)

    # Save to headings.txt
    with open("headings.txt", "w", encoding="utf-8") as f:
        for heading in valid_headings:
            f.write(heading + "\n")

    print("Success! Headings have been saved to headings.txt")
    print("Preview of extracted headings:")
    for h in valid_headings:
        print(f"- {h}")

else:
    print("Error: Could not find the main content div (mw-content-text).")
