# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Graphing
# ========
# MTS@Colorado.EDU
# 
# We'll be using the MatPlotLib library for plotting.
# Details on its API can be found [here](http://matplotlib.org/api/index.html).
# 
# Modules
# -------
# The main module is matplotlib.pyplot.
# pyplot contains all the plotting methods.
# 
# Sometimes people will use matplotlib.pylab, this is just pyplot with numpy added into it's namespace.
# 
# So, let us import some modules:

# <codecell>

import matplotlib.pyplot as plt
import numpy as np

# <codecell>

data = np.linspace(0,10,10)
print data

# <codecell>

plt.plot(data)

# <codecell>

plt.title("Line")
plt.xlabel("Index")
plt.ylabel("Value")
plt.plot(data)

# <codecell>

plt.title("Line")
plt.xlabel(r"Index $\beta$")
plt.ylabel(r"Value $\mu$")
plt.plot(data)

# <codecell>

fig = plt.figure("First Fig")
fig.add_subplot(2,1,1)
plt.plot(data)
plt.title('A')

fig.add_subplot(2,1,2)
plt.title('B')
plt.hist(data)

plt.show()

# <codecell>

plt.savefig("testimage.svg")

# <codecell>

plt.plot(data, '.')

# <codecell>

data_x1 = np.linspace(-10,10,10)
data_x2 = np.linspace(10,20,10)
data_y1 = [x**2 + 10 for x in data_x]
data_y2 = [x**2 - 10 for x in data_x]

plt.plot(data_x1, data_y1, 'r.', label='+10')
plt.xlim((-10,10))
plt.plot(data_x2, data_y2, 'b:', label='-10')
plt.xlim((0,20))

plt.legend()
plt.show()

# <codecell>

# Set a number of datapoints   
n = 10
t = np.linspace(0, 10, n)

# Set the parameters for the line
a = 1
b = 0

print "Initial Parameters: a = {:g} b = {:g}".format(a,b)

# Create a line a*t +b and add noise to it.
xerr = np.random.randn(n)
x = np.polyval([a, b], t) + xerr

xerr /= np.sqrt(2)

weights = [z**2 for z in x]

# Preform Linear Regression
#(ar, br) = np.polyfit(t, x, 1, w= weights)
(ar, br) = np.polyfit(t, x, 1)


# Create a line for the regression
xr = np.polyval([ar, br], t)

# root-mean-square-error
rmserr = np.sqrt(sum((xr-x)**2)/n)

print "Results of linear regression:",
print "a = {:g}, b = {:g}, rmserr = {:g}".format(ar, br, rmserr)

plt.figure(1)
plt.title("Linear Regression")
plt.plot(t, x, '.', label='Data')
plt.plot(t, xr, '--', label='Linear Fit')
plt.legend(loc='lower right')
plt.show()


plt.figure(1)
plt.errorbar(t, x, fmt='.', yerr=xerr )

# <codecell>

    

