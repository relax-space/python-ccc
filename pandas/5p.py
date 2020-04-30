import numpy as np
import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2',  'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
res = pd.merge(left, right, on='key')
print(res)

left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
res1 = pd.merge(left1, right1, on=['key1', 'key2'], how='inner')  # 内联合并
print(res1)
res2 = pd.merge(left1, right1, on=['key1', 'key2'], how='left')  # 左联合并
print(res2)
res3 = pd.merge(left1, right1, on=['key1', 'key2'], how='right')  # 右联合并
print(res3)

df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
# 依据col1进行合并 并启用indicator=True输出每项合并方式
res4 = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res4)
res5 = pd.merge(df1, df2, on='col1', how='outer',
                indicator='indicator_column')  # 自定义indicator column名称
print(res5)
