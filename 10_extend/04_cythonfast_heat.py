from numpy import zeros
from matplotlib import pyplot as P
from cProfile import run
from pstats import Stats

from cyupdate_fast import cy_updatefast

dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy
n = 300
niter=800
profile = '04_cython_profile.dat'

def calc(N, Niter=100, func=cy_updatefast, args=(dx2, dy2)):
    u = zeros([N, N])
    u[0] = 1
    for i in range(Niter):
        func(u,*args)
    return u
    
run('u = calc(n, Niter=niter)', profile)

cp = P.contourf(u)
cbar = P.colorbar()
P.show()

p = Stats(profile)
p.sort_stats('cumulative').print_stats(10)