import numpy as np
import pandas as pd

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
res = pd.merge(left, right, left_index=True, right_index=True,
               how='outer')  # 根据index索引进行合并 并选择外联合并
print(res)
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)
