# a rule to decide whether to buy or sell

import json
import requests
import os
import csv
import time
#from dotenv import load_dotenv
#load_dotenv()


#converting numbers into price (used in previous projects)
def to_usd(my_price):
    return f"${my_price:,.2f}" 

ticker = input("Please select a stock ticker: ")
if len(ticker) > 5: 
    print("Sorry, this is not a valid ticker, sorry.")
    quit()

api_key=os.environ.get("ALPHAVANTAGE_API_KEY")
request_url= f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={api_key}"
response = requests.get(request_url)
#parse response texts from string to dictionary
parsed_response = json.loads(response.text)

#finding time it was last refreshed
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


#finding latest prices
tsd=parsed_response["Time Series (5min)"] #have been exploring with smaller intervals because I am trying to adapt this code to crypto day-trading eventually using Binance API 
dates = list(tsd.keys())
latest_interval = dates[0] # pulling the most recent day from list, assuming latest day is first

latest_closing_price = tsd[latest_interval]["4. close"]
#finding recent high/low
high_prices = [] #getting high price for each interval
low_prices = []
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

recommendation = ""
recommendation_justification = ""

risk_tolerance = float(input("Please provide intra-day volatility tolerance (number will be converted to %)"))

risk_percentage = float(risk_tolerance / 100)
if(float(recent_high) - float(recent_low)) / float(recent_low) > float(risk_percentage):
    recommendation = "NO BUY"
    recommendation_justification = "This security is too volatile given your risk tolerance"
else:
    recommendation = "BUY"
    recommendation_justification = "This security falls within your risk tolerance"


#CSV file setup
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv") 

csv_headers=["timestamp","open","high","low","close","volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices=tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high":daily_prices["2. high"],
            "low":daily_prices["3. low"],
            "close":daily_prices["4. close"],
            "volume":daily_prices["5. volume"],
        })


#getting current date/time for line
request_date = time.strftime("%m/%d/%Y %I:%M %p")

#output
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {request_date}") 
print("-------------------------")
print(f"LATEST TIME:  {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_closing_price))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {recommendation}")
print(f"RECOMMENDATION REASON: {recommendation_justification}")
print("-------------------------")
print("WRITING DATA TO CSV...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")