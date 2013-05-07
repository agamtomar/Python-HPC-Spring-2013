from matplotlib import pyplot as P
from numpy import zeros
from cProfile import run
from pstats import Stats

dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy
n = 100
niter=300
profile = '01_purePython_profile.dat'

def py_update(u):
    nx, ny = u.shape
    for i in xrange(1,nx-1):
        for j in xrange(1, ny-1):
            u[i,j] = ((u[i+1, j] + u[i-1, j]) * dy2 +
                      (u[i, j+1] + u[i, j-1]) * dx2) / (2*(dx2+dy2))

def calc(N, Niter=100, func=py_update, args=()):
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

