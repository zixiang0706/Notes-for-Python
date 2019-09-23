import os
import pandas as pd

# get the name list of all the csv in specified path
csv_file_paths = []
for root, dirs, files in os.walk('./asset/history'):
    # 当files不为空的时候
    if files:
        for f in files:
            if f.endswith('.csv'):
                file_path = os.path.join(root, f)
                csv_file_paths.append(file_path)

# concatnate all the dataframe
all_df = pd.DataFrame()
for file in (csv_file_paths):
    print(file)
    # 导入数据
    df = pd.read_csv(file)
    #  合并数据
    all_df = all_df.append(df, ignore_index=True)

# 删除重复的数据
all_df.drop_duplicates(subset=['open_time'], inplace=True, keep='first')
all_df.describe()
# sorting
all_df.sort_values(by=['open_time'], ascending=1, inplace=True)
# transfer time to UTC
all_df['open_time'] = pd.to_datetime(all_df['open_time'], unit='ms')
# select columns
all_df = all_df[['open_time', 'open', 'high', 'low', 'close', 'volume']]
# set the index
all_df.set_index('open_time', inplace=True)
# save the data
all_df.to_csv('./asset/binance_btc_1min_2019.csv')
