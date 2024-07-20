from dotenv import load_dotenv
load_dotenv()

import os
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.amazon.in/'
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
TELEGRAM_API_SEND_MSG = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

items = [
    'Sony-WH-1000XM4-Cancelling-Headphones-Bluetooth/dp/B0863TXGM3/'
]

def main():
    for item in items:
        url = BASE_URL + item
        r = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'
        })
        soup = BeautifulSoup(r.text, 'html.parser')

        title = soup.find(id='productTitle').get_text().strip()
        price = soup.find(id='priceblock_ourprice').get_text().strip()

        data = {
            'chat_id': CHAT_ID,
            'text': f'[{title}]({url})\n*{price}*',
            'parse_mode': 'Markdown'
        }
        r = requests.post(TELEGRAM_API_SEND_MSG, data=data)

if __name__ == '__main__':
    main()

