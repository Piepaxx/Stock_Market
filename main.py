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


#Getting the STOCK DATA
resource = requests.get(url, params= params)
resource.raise_for_status()
print(resource.json())

#Get the previous day
last_refresh = resource.json()["Meta Data"]["3. Last Refreshed"]
date_obj = datetime.strptime(last_refresh, "%Y-%m-%d")
previous_day_time = date_obj - timedelta(days=1)
previous_day = previous_day_time.strftime("%Y-%m-%d")

stock_data = resource.json()["Time Series (Daily)"]

last_stock_data = stock_data[last_refresh]
last_closing = last_stock_data["4. close"]

previous_day_data = stock_data[previous_day]
previous_day_closing = previous_day_data["4. close"]

change = float(previous_day_closing) - float(last_closing)
percent_change = change/100 * previous_day_closing

if 5 > percent_change > -5:
    print("HUGE STOCK DIFFERENCE FOR TESLA")