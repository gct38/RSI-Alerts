RSI Alerts
================================================

Purpose
----------------------------------------

The RSI Alerts is a simple python script that can alert users through email or text message
when stocks in your Alpaca watchlist meets the following criteria:

* Current RSI is below 30
* Current RSI is below the 3 month RSI average

Current Scope
----------------------------------------

We will be using Alpaca's Trading API to utilize the trades and AlphaVantage's API to
obtain RSI data.

These two criteria were created as a guideline for when a stock is undersold. Once it is
deemed undersold, it will notify the user through either text message or email.

In the current scope, we plan on making the script automatically put in a buy order of an
arbitrary amount of shares TBD. This will all be done on Alapca's Paper Trading account
such that no real money is involved.

Future Scope
----------------------------------------

TBD