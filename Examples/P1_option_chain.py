from dpf.scripting import AnalyticalVanilla

import pandas as pd
import numpy as np
from yahoo_fin import options
import datetime


tesla = options.get_options_chain("TSLA")

tesla_call = tesla['calls']
tesla_put = tesla['puts']

tesla_call.columns


# datetime manipulation
expiration_raw = options.get_expiration_dates("TSLA")
expiration_list = [datetime.datetime.strptime(date,  "%B %d, %Y") for date in expiration_raw]

start = datetime.datetime.today().date()
end = expiration_list[0].date()

days = np.busday_count(start, end)


time_to_maturity = []
for day in expiration_list:
    end = day.date()
    days = np.busday_count(start, end)
    time_to_maturity.append(days)


target_date = expiration_raw[7]
options_data = options.get_options_chain("TSLA", target_date)
options_data['calls'].sort_values(by='Open Interest')
options_data['calls']['Strike'].unique()

Strike_list = list(map(float, range(600,1400,50)))

time_to_maturity[8]


target_date = expiration_raw[8]
options_data = options.get_options_chain("TSLA", target_date)
options_data['calls'].sort_values(by='Open Interest')
options_data['calls']['Last Price']

call_option_3m = options_data['calls']
call_option_3m = call_option_3m[call_option_3m['Strike'].isin(Strike_list)][['Strike', 'Last Price', 'Implied Volatility']]

put_option_3m = options_data['puts']
put_option_3m = put_option_3m[put_option_3m['Strike'].isin(Strike_list)][['Strike', 'Last Price', 'Implied Volatility']]

call_option_3m
put_option_3m


put_option_3m.plot(x='Strike', y='Implied Volatility')
pd.concat([put_option_3m, call_option_3m], axis=1)


from inspect import getmembers, isfunction

from dpf import scripting


