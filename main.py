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

#Get the previous day
last_refresh = resource.json()["Meta Data"]["3. Last Refreshed"]
date_obj = datetime.strptime(last_refresh, "%Y-%m-%d")
previous_day_time = date_obj - timedelta(days=1)
previous_day = previous_day_time.strftime("%Y-%m-%d")

stock_data = resource.json()["Time Series (Daily)"][last_refresh]
print(stock_data)