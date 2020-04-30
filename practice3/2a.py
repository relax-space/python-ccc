import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height,
                 str(height), ha="center", va="bottom")


dates = pd.date_range('20200425', periods=6)
s = pd.Series([100, 80, 90, 70, 50, 85])
# plt.figure(figsize=(8, 8))
bar1 = plt.bar(dates, s, label='A', width=0.6)
plt.xticks(rotation=90)  # 这里是调节横坐标的倾斜度，rotation是度数
plt.legend()
autolabel(bar1)
plt.show()
