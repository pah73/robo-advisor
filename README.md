# robo-advisor
Robo Advisor Project

This readme page explains how to use the robo-advisor. The user can fetch stock data from the Alpha Vantage APIs for any stock and returns last closing price, recent highs and lows, and a buy or don't buy recommendation. The recommendation is based off of a % risk tolerance that is calculated based on volatility for the period. 

# Prerequisites:
```sh
Anaconda 3.7+
Python 3.7+
Pip
```

# Installing the Repository
Fork this remote repository under your own control, then clone remote copy onto your local computer using the GitHub desktop app. 

Navigate to the repository from the command line (subsequent commands assume you are running them from the local repository's root directory). If you saved the repository to your desktop use the following code or else you will have to adjust the code to wherever the repository is saved:
```sh
cd ~/Desktop/robo-advisor
```
# Create and activate virtual enviorment
Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

```sh
conda create -n stocks-env python=3.8
conda activate stocks-env
```

From inside the virtual environment, install package dependencies. The requirmemnts.txt file has the Dotenv package which is needed to load enviorment variables as well as the requests package which is nrequest data from the internet:
```sh
pip install -r requirements.txt
```
# Setup local variables
In the root directory of your local repository, create a new file called ".env". The program needs an API key to issue requests to AlphaVantage API. Follow this link and the instructions to get a free API key:  https://www.alphavantage.co/ and create a variable called ALPHAVANTAGE_API_KEY in the .env file with your API key:

```sh
ALPHAVANTAGE_API_KEY="YOUR_API_KEY"
```

The user can choose whichever API key they would like to use. For the purposes of my project, I used 5 minute intervals on stock data, in order to make this robot useful for day trading, rather than getting daily prices. 

# Run the robo-advisor Python Script and follow the instructions to input valid stock symbols (eg. "MSFT") for the desired stocks:
```sh
python shopping_cart.py
```
The program will fail if the stock symbol is unrecognized or more than 5 letters.

Afterwards, the program will ask the user to input risk tolerance, which it will convert from numeric value to %, and base the recommendation based off of this metric. 

