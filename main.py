import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta


load_dotenv()
STOCK_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
url = 'https://www.alphavantage.co/query?'
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API_KEY
        }

# #Getting the STOCK DATA
resource = requests.get(url, params= params)
resource.raise_for_status()
#
#Get the previous day
date_obj = datetime.strptime('2025-10-31', "%Y-%m-%d")
previous_day_time = date_obj - timedelta(days=1)
previous_day = previous_day_time.strftime("%Y-%m-%d")

stock_data = resource.json()["Time Series (Daily)"]

last_stock_data = stock_data['2025-10-31']
last_closing = last_stock_data["4. close"]

previous_day_data = stock_data[previous_day]
previous_day_closing = previous_day_data["4. close"]

change = float(last_closing) - float(previous_day_closing)
percent_change = change/float(previous_day_closing)*100

news_url = 'https://newsapi.org/v2/everything?'
today = datetime.today()
news_params = {
    "q": "tesla stock",
    "searchIn": "title",
    "apikey": os.environ.get("NEWS_API_KEY"),
    "from": previous_day,
    "sortBy": "relevancy",
    "pageSize": 3
}


if 5 < percent_change < -5:
    print("HUGE STOCK DIFFERENCE FOR TESLA")
    news_resource = requests.get(news_url, params=news_params)
    for _ in range(3):
        print(f"news titles: {news_resource.json()["articles"][_]["title"]}\n"
              f"link: {news_resource.json()["articles"][_]["url"]}\n")
else:
    print(f"the stock change from the previous closing day has a change of: {percent_change:.2f}%,"
          f" no significant change in stock prices")




