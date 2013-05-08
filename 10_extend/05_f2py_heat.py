from numpy import zeros, asfortranarray
from matplotlib import pyplot as P
from cProfile import run
from pstats import Stats

from f2py_update import f2py_update90

dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy
n = 300
niter=10000
profile = '05_f2py_profile.dat'

def calc(N, Niter=100, func=f2py_update90, args=(dx2, dy2)):
    u = zeros([N, N])
    u[0] = 1.0
    u = asfortranarray(u)
    for i in range(Niter):
        func(u,*args)
    return u
    
run('u = calc(n, Niter=niter)', profile)

cp = P.contourf(u)
cbar = P.colorbar()
P.show()

p = Stats(profile)
p.sort_stats('cumulative').print_stats(10)