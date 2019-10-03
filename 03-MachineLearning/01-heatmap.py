# import the dependance
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={'axes.facecolor': 'cornflowerblue', 'figure.facecolor': 'cornflowerblue'})

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
# pd.set_option('display.max_rows', 1000)  # 最多显示行数.
# pd.set_option('precision', 6)  # 浮点数的精度
pd.set_option('display.float_format', lambda x: '%.4f' % x)  # 设置不用科学计数法，保留两位小数.

df = pd.read_csv('./asset/binance_btc_1min.csv')
df['open_time'] = pd.to_datetime(df['open_time'])
df = df[df['open_time'] >= pd.to_datetime('2019-06-07 15:00:00')]

df.set_index('open_time', inplace=True)
df_s = df.resample(rule='6H').agg({'open': 'first', 'high': 'max', 'low': 'min',
                                   'close': 'last', 'volume': 'sum', })

df_s['date'] = df_s.index.date
df_s['hour'] = df_s.index.time
result = df_s.pivot(index='date', columns='hour', values='close')
sns.heatmap(result, annot=False, fmt="g", cmap='viridis', cbar=True)
plt.show()
