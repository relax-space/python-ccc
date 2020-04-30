import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height,
                 str(height), ha="center", va="bottom")


dates = pd.date_range('20200425', periods=6)
label_list = [d.strftime("%Y-%m-%d") for d in dates]
s1 = pd.Series([100, 90, 70, 100, 50, 99])
s2 = pd.Series([85, 20, 60, 30, 90, 100])
x = range(len(s1))

bar1 = plt.bar(x, s1, align='center', width=0.4, label="A")
bar2 = plt.bar([i+0.4 for i in x], s2, align='center', width=0.4, label="B")
plt.legend()
plt.xticks([i + 0.2 for i in x], label_list, rotation=90)

autolabel(bar1)
autolabel(bar2)

plt.show()
