import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from scipy import stats
import pandas as pd
import os
import style
#from pylab import *
from matplotlib.patches import Polygon

cars = pd.read_csv(os.path.join('data','cars.csv'))

c4 = cars[cars['cyl'] == 4]['mpg']
c6 = cars[cars['cyl'] == 6]['mpg']
c8 = cars[cars['cyl'] == 8]['mpg']

mu, sigma = 100, 15
x1 = 100 + 15 * np.random.randn(100)
x2 = 50 + 10 * np.random.randn(75)

data = [c4,c6,c8]

fig, ax = plt.subplots()
ax.set_xlabel('cyl')
ax.set_ylabel('mpg')
ax.set_title('Box')
#ax.set_xticks([1,2,3],('4','6','8'))
#ax.tickNames = plt.setp(ax, xticklabels=keywords['names'] )
#
#ggplot.rbox(ax, data, names=['4','6','8'])
colors = ['#1B9E77','#D95F02','#7570B3']

bp = ax.boxplot(data, widths=0.65)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black', linestyle = 'solid')
plt.setp(bp['fliers'], color='black', alpha = 0.9, marker= 'o', markersize = 3)
plt.setp(bp['medians'], color='black')
plt.setp(ax, xticklabels=['c4','c6','c8'] )

numBoxes = len(data)
for i in range(numBoxes):
    box = bp['boxes'][i]
    boxX = []
    boxY = []
    for j in range(5):
      boxX.append(box.get_xdata()[j])
      boxY.append(box.get_ydata()[j])
    boxCoords = zip(boxX,boxY)

    boxPolygon = Polygon(boxCoords, facecolor = colors[i % len(colors)])
    ax.add_patch(boxPolygon)

fig.savefig(os.path.join('img','box.pdf'))

style.ggplot(ax)
fig.savefig(os.path.join('img','box_ggplot.pdf'))

#style.xkcd(ax)
#fig.savefig(os.path.join('img','box_xkcd.pdf'))


#fig.show()