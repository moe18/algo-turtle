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
        hist_data = self.tickers.history(period='1y', interval='1d')
        return hist_data

    def get_hist_data_by_date_yahoo(self):
        hist_data = self.tickers.history(start=self.start, end=self.end)
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

    def get_asset_prof_data_yahoo(self):
        asset_prof = self.tickers.asset_profile
        return asset_prof

    def get_cal_events_yahoo(self):
        cal_events = self.tickers.calendar_events
        return cal_events

    def get_earning_hist_yahoo(self):
        earning_hist = self.tickers.earning_history
        return earning_hist

    def get_earnings_trend_yahoo(self):
        earnings_trend = self.tickers.earnings_trend
        return earnings_trend




