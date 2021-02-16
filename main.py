#TODO: implement going thru watchlist to see if stock is undersold
#TODO: first utilize some type of other filter to trim watchlists (alphavantage API max of 5 calls/min or 500 calls/day
#FIXME: raise issue to Alpaca that gives me 403 (Forbidden) access to data.alpaca.markets API

import settings
from rsi import RSIData
import alpaca_trade_api as tradeapi
import alpaca

if __name__ == '__main__':
    api = tradeapi.REST(base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
    account = api.get_account()
    api.list_positions()
    #print(account)

    bars_api = tradeapi.REST(base_url=f"https://data.alpaca.markets/v1/bars")



    watchlist = alpaca.get_watchlist_symbols('To Buy', api)
    equity = watchlist[0]
    print(equity)

    bars = bars_api.get_barset('AAPL', 'day', limit=10).df
    #aggs = apiv2.get_aggs(equity, 'day', 1, '2021-01-01', '2021-02-01')



    #rsi = RSIData(equity)
    #print(rsi.undersold())

