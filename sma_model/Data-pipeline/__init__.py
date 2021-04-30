import get_data
import clean_data

data = get_data.GetFinData()
data.stocks = ['aapl']

hist_data = data.get_hist_data_yahoo()
c_data_class = clean_data.CleanFinData()

c_data_class.data = hist_data.reset_index().set_index('date')

print(c_data_class.get_daily_vol(c_data_class.data.close))
