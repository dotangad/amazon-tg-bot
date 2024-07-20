# Amazon Price Tracker

Heavily inspired by [leon-sleepinglion/price-monitoring-telegram-bot](https://github.com/leon-sleepinglion/price-monitoring-telegram-bot/).

## Setup

1. Fill out .env

```
TOKEN=
CHAT_ID=
```

2. Add your URLs to main.py

```python
items = [
    'Sony-WH-1000XM4-Cancelling-Headphones-Bluetooth/dp/B0863TXGM3/'
]
```

3. Add the script to your crontab

```sh
crontab -e
```
