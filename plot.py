import pandas as pd
import matplotlib.pyplot as plt

perc=pd.read_csv("./results/perc.csv")
perc.sort_values(ascending=False, by='V')[:20].plot.bar(x='T',y='V')
plt.show()