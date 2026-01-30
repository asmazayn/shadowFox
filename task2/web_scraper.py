import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        data = []

        for link in soup.find_all("a"):
            text = link.text.strip()
            href = link.get("href")

            if text and href:
                data.append({"Text": text, "Link": href})

        return data

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def save_to_csv(data, filename="scraped_data.csv"):
    if data:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print("Data saved to", filename)
    else:
        print("No data to save")

if __name__ == "__main__":
    url = "https://shadowfox.in"
    scraped_data = scrape_website(url)
    save_to_csv(scraped_data)
