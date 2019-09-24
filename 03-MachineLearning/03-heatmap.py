# import the dependance
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np

warnings.simplefilter(action="ignore", category=RuntimeWarning)
# sns.set(rc={'axes.facecolor':'cornflowerblue', 'figure.facecolor':'cornflowerblue'})
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
# pd.set_option('display.max_rows', 1000)  # 最多显示行数.
# pd.set_option('precision', 6)  # 浮点数的精度
pd.set_option('display.float_format', lambda x: '%.4f' % x)  # 设置不用科学计数法，保留两位小数.
plt.figure(figsize=(16, 8))

# parameter
TIME = '1H'
THRESHOLD = 0.5
COMPARE_TIME = 1
MODE = {0: 'fluc_pct',
        1: 'fluc_cumsum',
        2: 'margin'}[2]

# read data
df = pd.read_csv('./asset/binance_btc_1min_2019.csv')

# cut the reducdant info
df['open_time_local'] = pd.to_datetime(df['open_time'])
df = df[df['open_time_local'] >= pd.to_datetime('2019-08-16 00:00:00')]

# sampling by 1h
df.set_index('open_time_local', inplace=True)
df['high_time'] = df['high']
df['low_time'] = df['low']

df_s = df.resample(rule=TIME).agg({'open': 'first', 'high': 'max', 'low': 'min',
                                   'close': 'last', 'volume': 'sum',
                                   'high_time': lambda s: s.idxmax(),
                                   "low_time": lambda s: s.idxmin()})
df_s["rise"] = (df_s['high_time'] > df_s["low_time"])
df_s['rise'] = df_s['rise'].apply(lambda x: 1 if x else -1)
df_s['margin'] = (df_s['high']-df_s['low'])*df_s['rise']/df_s['low']*100

# separate time info
df_s['date'] = df_s.index.date
df_s['hour'] = df_s.index.time
df_s["fluc_pct"] = df_s['close'].pct_change(COMPARE_TIME) * 100
df_s["fluc_cumsum"] = df_s['fluc_pct'].cumsum()
print(df_s.head())
print(df.head())

if MODE == 'fluc_pct':
    result = df_s.pivot(index='date', columns='hour', values='fluc_pct')
    mask = (result.values >= (-1.0 * THRESHOLD)) & (result.values <= THRESHOLD)
elif MODE == 'fluc_cumsum':
    result = df_s.pivot(index='date', columns='hour', values='fluc_cumsum')
    mask = False
elif MODE == 'margin':
    result = df_s.pivot(index='date', columns='hour', values='margin')
    mask = (result.values >= (-1.0 * THRESHOLD)) & (result.values <= THRESHOLD)

sns.heatmap(result, mask=mask, annot=False, fmt=".1f", cbar=True,
            center=0, cmap="RdBu_r", linewidths=.01, linecolor='gray')
plt.xticks(rotation=15)
plt.yticks(rotation=0)
plt.show()
