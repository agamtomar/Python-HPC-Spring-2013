import os
import pandas as pd
import matplotlib.pyplot as pl
import numpy as np        
from scipy import stats
import style


cars = pd.read_csv(os.path.join('data','cars.csv'))

cars4 = cars[cars['cyl'] == 4]
cars6 = cars[cars['cyl'] == 6]
cars8 = cars[cars['cyl'] == 8]

x = cars['wt'].values
y = cars['mpg'].values
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
ye = slope*x + intercept

fig, ax = pl.subplots()
ax.scatter(cars4['wt'], cars4['mpg'], c='#1B9E77', label='4 cyl', s=200, alpha=0.75, edgecolors='none',lw=.7, marker='o')
ax.scatter(cars6['wt'], cars6['mpg'], c='#D95F02', label='6 cyl', s=200, alpha=0.75, edgecolors='none')
ax.scatter(cars8['wt'], cars8['mpg'], c='#7570B3', label='8 cyl', s=200, alpha=0.75, edgecolors='none')

ax.plot(x, ye, label="estimate", c='black')

lab = '%.2f'%(slope) + '*x + ' + '%.2f'%(intercept)
ax.annotate(r'$y = ' + lab + '$',
         xy=(3.25,20), xycoords='data',
         xytext=(-150,-100), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2"))

ax.legend(loc='best', scatterpoints=1)

fig.savefig(os.path.join('img','scatter.pdf'))  

style.ggplot(ax)  
fig.savefig(os.path.join('img','scatter_ggplot.pdf'))  

#style.xkcd(ax)  
#fig.savefig(os.path.join('img','scatter_xkcd.pdf'))  
fig.show()

