
import pandas as pd
import numpy as np


class CleanFinData:
    """
    Deal with outliers and N.A. values and any other cleaning that
    has to be done. Get data from get_data -> Then feed into label_data
    """

    def __init__(self):
        self.data = pd.DataFrame()

    @staticmethod
    def get_daily_vol(close, span=100):
        """
        daily vol, reindexed to close
        :param close: close price pd Series
        :param span: the days the exponential weighted moving std look back
        :return: the ewm std of a stocks returns
        """
        df0 = close.index.searchsorted(close.index-pd.Timedelta(days=1))
        df0 = df0[df0 > 0]
        df0 = pd.Series(close.index[df0-1], index=close.index[close.shape[0]-df0.shape[0]:])

        # day return
        df0 = close.loc[df0.index]/close.loc[df0.values].values-1
        df0 = df0.ewm(span=span).std()
        return df0





    @staticmethod
    def bar(xs, y):
        return np.int64(xs / y) * y

    def tick_bar(self):
        # ohlc = open high low close
        return self.data.groupby(self.bar(np.arange(len(self.data)), 10)).agg({'price': 'ohlc', 'size': 'sum'})

    def vol_bar(self, n):
        """

        :param n: number of shares traded
        :return:
        """
        # ohlc = open high low close
        return self.data.groupby(self.bar(np.ndarray.cumsum(self.data['size']), n)).agg({'price': 'ohlc', 'size': 'sum'})

    def dol_bar(self, n):
        """

        :param n: number of dollars traded
        :return:
        """
        # ohlc = open high low close
        return self.data.groupby(self.bar(np.ndarray.cumsum(self.data['price']), n)).agg({'price': 'ohlc', 'size': 'sum'})

