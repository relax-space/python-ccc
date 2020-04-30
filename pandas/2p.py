import numpy as np
import pandas as pd

dates = pd.date_range('20200401', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates,
                  columns=['A', 'B', 'C', 'D'])
print(df)
print(df[0:3])
print(df['20200402':'20200404'])  # 两次进行选择 第一次切片选择 第二次按照筛选条件进行选择
print(df.loc['20200402', ['A', 'B']])  # 按照行标签进行选择 精确选择
print(df.iloc[3, 1])  # 输出第三行第一列的数据
print(df.iloc[3:5, 0:2])  # 进行切片选择
print(df.iloc[[1, 2, 4], [0, 2]])  # 进行不连续筛选
print(df[df.A > 0])  # 筛选出df.A大于0的元素 布尔条件筛选

df.iloc[2, 2] = 999  # 单点设置
df.loc['20200401', 'D'] = 999
print(df)
df[df.A > 0] = 999  # 将df.A大于0的值改变
print(df)
df['F'] = np.nan
print(df)
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range(
    '20200401', periods=6))  # 增加一列
print(df)
