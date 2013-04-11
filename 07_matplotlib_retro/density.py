import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os
import style

mu, sigma = 100, 15
x1 = 100 + 15 * np.random.randn(100)
x2 = 50 + 10 * np.random.randn(100)

density1 = stats.kde.gaussian_kde(x1)
density2 = stats.kde.gaussian_kde(x2)

fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Density')

x = np.linspace(0, 200, 200)
ax.plot(x, density1(x), color='#1B9E77', label='d1')
ax.plot(x, density2(x), color='#D95F02', label='d2')

ax.fill_between(x, 0, density1(x), alpha=0.5, color='#1B9E77')
ax.fill_between(x, 0, density2(x), alpha=0.5, color='#D95F02')

ax.plot([100,100],[0,density1(100)], color ='#1B9E77', linewidth=1, linestyle="--")
ax.plot([50,50],[0,density2(50)], color ='#D95F02', linewidth=1, linestyle="--")

fig.savefig(os.path.join('img','density.pdf'))

style.ggplot(ax)
fig.savefig(os.path.join('img','density_ggplot.pdf'))

style.xkcd(ax)
fig.savefig(os.path.join('img','density_xkcd.pdf'))
#fig.show()