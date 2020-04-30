import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def autolabel(rects):
    for rect in rects.patches:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height,
                 str(height), ha="center", va="bottom")


dates = [d.strftime("%Y-%m-%d") for d in pd.date_range('20200425', periods=6)]
df = pd.DataFrame({'A': [100, 90, 70, 100, 50, 99],
                   'B': [85, 20, 60, 30, 90, 100]}, index=dates)
df = df[df.A > 80]
bar1 = df.plot(kind='bar')
autolabel(bar1)

plt.show()
