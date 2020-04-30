import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
# 0表示竖项合并 1表示横项合并 ingnore_index重置序列index index变为0 1 2 3 4 5 6 7 8
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)
res_1 = df1.append(df2, ignore_index=True)
print(res_1)

df4 = pd.DataFrame(np.ones((3, 4))*0,
                   columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df5 = pd.DataFrame(np.ones((3, 4))*1,
                   columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])

res1 = pd.concat([df4, df5], axis=1, join='outer')  # 行往外进行合并
print(res1)
res2 = pd.concat([df4, df5], axis=1, join='inner')  # 行相同的进行合并
print(res2)

df6 = pd.DataFrame(np.ones((3, 4))*0,
                   columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df7 = pd.DataFrame(np.ones((3, 4))*1,
                   columns=['a1', 'b1', 'c1', 'd1'], index=[2, 3, 4])
res3 = df6.join(df7)
print(res3)
res3 = df6.join(df7, how='right')
print(res3)
