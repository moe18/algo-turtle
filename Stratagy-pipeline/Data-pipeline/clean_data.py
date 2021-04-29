
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

