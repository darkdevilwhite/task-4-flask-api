import requests
from bs4 import BeautifulSoup

url = "https://www.theverge.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Verge uses <h2> for headlines with class "duet--content-cards--content-card-title"
    headlines = soup.find_all("h2")

    clean_headlines = [h.text.strip() for h in headlines if h.text.strip()]

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for headline in clean_headlines:
            file.write(headline + "\n")

    print(f"{len(clean_headlines)} headlines saved to headlines.txt")

except requests.RequestException as e:
    print("Failed to fetch headlines:", e)
