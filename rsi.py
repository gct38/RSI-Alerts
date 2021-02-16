from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


class RSIData:
    def __init__(self, equity):
        self.ti = TechIndicators(output_format='pandas')
        self.current = None
        self.info = None
        self.equity = equity
        self.rsi = self.rsi_data()
        self.avg = self.avg_rsi()

    def rsi_data(self):
        data, info = self.ti.get_rsi(symbol=self.equity)
        self.current = data.tail(1)['RSI'].values[0]
        self.info = info
        return data

    def plot_rsi(self):
        plt.figure(figsize=(10, 6))
        plt.legend(loc='best')
        plt.plot(self.rsi, color='blueviolet', label=self.equity + ' RSI Indicator')
        plt.hlines(y=[70], xmin=self.rsi.index[0], xmax=self.rsi.index[len(self.rsi.index) - 1], colors=['green'],
                   label='RSI High')
        plt.hlines(y=[30], xmin=self.rsi.index[0], xmax=self.rsi.index[len(self.rsi.index) - 1], colors=['red'],
                   label='RSI Low')
        plt.title(self.equity + ' RSI (Relative Strength Index)')
        plt.xlabel('Time')
        plt.ylabel('RSI Values')
        plt.legend()
        plt.show()

    def avg_rsi(self):
        """ Takes the average RSI value of the past 3 months and returns that value as a float """
        rsi = self.rsi
        end = pd.to_datetime(date.today())
        start = pd.to_datetime(date.today() - relativedelta(months=3))  #goes back 3 months from today
        rsi = rsi.loc[(rsi.index > start) & (rsi.index < end)]  #filter out all dates that aren't between start and end
        average = rsi['RSI'].mean()
        self.avg = average
        return average

    def undersold(self):
        """
        Compares current (today) RSI to AVG RSI to determine if equity is undersold.

        If current RSI is below 30 (arbitrary value of undersold) or
            below the 3 month average, return True
        """
        print("current RSI {:}, avg: {:}".format(self.current, self.avg))
        return self.current < 30 or self.current < self.avg

