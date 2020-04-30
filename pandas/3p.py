import numpy as np
import pandas as pd

dates = pd.date_range('20200401', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates,
                  columns=['A', 'B', 'C', 'D'])

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
# 0对行进行操作 1对列进行操作 any:只要存在NaN即可drop掉 all:必须全部是NaN才可drop
print(df.dropna(axis=0, how='any'))
print(df.fillna(value=0))  # 将NaN值替换为0
print(pd.isnull(df))  # 矩阵用布尔来进行表示 是nan为ture 不是nan为false

df.to_csv('./pandas/test.csv')
df1 = pd.read_csv('./pandas/test.csv')
print(df1)
