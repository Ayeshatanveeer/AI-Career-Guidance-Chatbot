import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/career-advice"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()

with open("data.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Data scraped successfully!")