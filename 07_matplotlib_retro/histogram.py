import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import style


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(300)

density = stats.kde.gaussian_kde(x)
fig, ax = plt.subplots()

n, bins, patches = ax.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('histogram')

xd = np.linspace(min(x)-10, max(x)+10, 30)
ax.plot(xd, density(xd))

fig.savefig(os.path.join('img','histogram.pdf'))

style.ggplot(ax)
fig.savefig(os.path.join('img','histogram_ggplot.pdf'))

# style.xkcd(ax)
# fig.savefig(os.path.join('img','histogram_xkcd.pdf'))
#fig.show()