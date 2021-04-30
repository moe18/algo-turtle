import pandas as pd
from yahooquery import Ticker


class GetFinData:
    """
    Get any type of fin data, for example
    - Fundamental Data
    - Market Data
    - Analytics
    - Alternative Data
    """
    def __init__(self):
        self.data = []
        self.stocks = ['']
        self.tickers = None
        self.start_date = '2020-01-01'
        self.end_date = '2021-01-01'

    def make_ticker_yahoo(self):
        self.tickers = Ticker(self.stocks, asynchronous=True)

    def get_hist_data_yahoo(self, period='1y', interval='1d'):
        ticker = Ticker(self.stocks, asynchronous=True)
        hist_data = ticker.history(period=period, interval=interval)
        return hist_data

    def get_hist_data_by_date_yahoo(self):
        hist_data = self.tickers.history(start=self.start, end=self.end)
        return hist_data

    def save_data_to_csv(self, file_name):
        self.data.to_csv(
            '/Users/mordechaichabot/turtle-algo/algo-turtle/Stratagy-pipeline/Data-pipeline/raw_data/'+file_name)
