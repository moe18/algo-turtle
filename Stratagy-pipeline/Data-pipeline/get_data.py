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
        self.tickers = ''
        self.start_date = ''
        self.end_date = ''

    def make_ticker_yahoo(self):
        self.tickers = Ticker(self.stocks, asynchronous=True)

    def get_hist_data_yahoo(self, period='1y', interval='1d'):
        hist_data = self.tickers.history(period='1y', interval='1d')
        return hist_data

    def get_balance_sheet_data_yahoo(self, freq='a'):
        bal_data = self.tickers.balance_sheet(frequency=freq)
        return bal_data

    def get_cash_flow_data_yahoo(self, freq='a'):
        cash_data = self.tickers.cash_flow(frequency=freq)
        return cash_data

    def get_income_statement_data_yahoo(self, freq='a'):
        income_data = self.tickers.income_statement(frequency=freq)
        return income_data

    def get_valuation_measures_data_yahoo(self):
        val_measures = self.tickers.valuation_measures
        return val_measures




