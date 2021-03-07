import json
import requests
import os

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

api_key=os.environ.get("ALPHAVANTAGE_API_KEY")
request_url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)
parsed_response = json.loads(response.text)

tsd=parsed_response["Time Series (Daily)"]