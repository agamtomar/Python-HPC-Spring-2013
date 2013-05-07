from numpy import zeros
from matplotlib import pyplot as P
from cProfile import run
from pstats import Stats

dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy
n = 300
niter=800
profile = '02_numpy_profile.dat'

def numpy_update(u):
    u[1:-1,1:-1] = ((u[2:,1:-1]+u[:-2,1:-1])*dy2 + 
                    (u[1:-1,2:] + u[1:-1,:-2])*dx2) / (2*(dx2+dy2))
    

def calc(N, Niter=100, func=numpy_update, args=()):
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