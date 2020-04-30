import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3, np.nan, 5, 6])
print(s)

dates = pd.date_range('20200401', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates,
                  columns=['A', 'B', 'C', 'D'])  # 生成6行4列位置
print(df)
print(df['B'])

df_1 = pd.DataFrame({'A': 1.,
                     'B': pd.Timestamp('20200401'),
                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                     'D': np.array([3]*4, dtype='int32'),
                     'E': pd.Categorical(['test', 'train', 'test', 'train']),
                     'F': 'foo'})
print(df_1)
print(df_1.dtypes)
print(df_1.values)  # 把每个值进行打印出来
print(df_1.describe())  # 数字总结
print(df_1.T)  # 翻转数据
# axis等于1按列进行排序 如ABCDEFG 然后ascending倒叙进行显示
print(df_1.sort_index(axis=1, ascending=False))
print(df_1.sort_values(by='E'))  # 按值进行排序
