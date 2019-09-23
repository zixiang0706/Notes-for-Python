# import the dependance
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(rc={'axes.facecolor':'cornflowerblue', 'figure.facecolor':'cornflowerblue'})
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
# pd.set_option('display.max_rows', 1000)  # 最多显示行数.
# pd.set_option('precision', 6)  # 浮点数的精度
pd.set_option('display.float_format', lambda x: '%.4f' % x)  # 设置不用科学计数法，保留两位小数.

# parameter
TIME = '2H'
THRESHOLD = 0.5


# read data
df = pd.read_csv('./asset/binance_btc_1min_2019.csv')

# cut the reducdant info
df['open_time_local'] = pd.to_datetime(df['open_time'])
df = df[df['open_time_local']>=pd.to_datetime('2019-08-16 00:00:00')]

# sampling by 1h
df.set_index('open_time_local', inplace=True)
df_s = df.resample(rule=TIME).agg({'open': 'first','high': 'max','low': 'min',
                                   'close': 'last','volume': 'sum',})

# separate time info
df_s['date'] = df_s.index.date
df_s['hour'] = df_s.index.time
# calcu the fluc
df_s["fluc_pct"] =df_s['close'].pct_change(1)*100

result = df_s.pivot(index='date', columns='hour', values='fluc_pct')
mask = (result.values >= -1*THRESHOLD) & (result.values <= THRESHOLD)
sns.heatmap(result, mask=mask, annot=True, fmt=".1f", cbar=True, center=0)
plt.show()
