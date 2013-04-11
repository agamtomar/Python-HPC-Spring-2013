# Installed
import os
import pandas as pd
import matplotlib.pyplot as plt

# Local
import style

names = pd.read_csv(os.path.join('data','names.csv'))

fig, ax = plt.subplots()
ax.plot(names.year, names.M, label="M", linewidth=2.0)
ax.plot(names.year, names.F, label="F", linewidth=2.0)
ax.legend(loc='best')

fig.savefig(os.path.join('img','line.pdf'))

style.ggplot(ax)

fig.savefig(os.path.join('img','line_ggplot.pdf'))

style.xkcd(ax)
fig.savefig(os.path.join('img','line_xkcd.pdf'))

