import requests
from bs4 import BeautifulSoup
import json

URL = "https://pallavigodambe25.github.io/College-website/"

def scrape_notices():

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    notices = []

    # Extract headings
    headings = soup.find_all(["h1","h2","h3"])

    for h in headings:
        text = h.get_text(strip=True)
        if len(text) > 5:
            notices.append(text)

    # Extract paragraphs
    paragraphs = soup.find_all("p")

    for p in paragraphs:
        text = p.get_text(strip=True)
        if len(text) > 40:
            notices.append(text)

    with open("../data/notices.json","w",encoding="utf-8") as f:
        json.dump(notices,f,indent=4)

    print("✅ Extracted", len(notices), "content blocks")


if __name__ == "__main__":
    scrape_notices()