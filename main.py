import requests
from bs4 import BeautifulSoup
from pprint import pprint

product_url = "https://www.amazon.com/ASUS-Gaming-GeForce-Graphics-DisplayPort/dp/B0BLGQHS53/ref=sr_1_1?crid=R8G0U6ALI73E&keywords=rtx+4080&qid=1687395485&sprefix=rtx+408%2Caps%2C621&sr=8-1"
header = {
    'Accept-Language': "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

price_can_buy = 1500
response = requests.get(url=product_url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
price_now = soup.find(name="span", class_="a-offscreen").getText().split("$")[1]

if price_can_buy > float(price_now):
    pass
    # send_email

