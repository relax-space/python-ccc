import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, 7, 6, 9])
plt.plot(s)
plt.grid()
plt.show()

# s.plot(grid=True)
# plt.show()
