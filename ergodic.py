import numpy as np
import pylab
from scipy import integrate
from data import getdata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def vectorfield(x, t, sigma, rho, beta):
    """
    Function to return the value of dx/dt, given x.
    
    Inputs:
    x - the value of x
    t - the value of t
    alpha - a parameter
    beta - another parameter

    Outputs:
    dxdt - the value of dx/dt
    """
    
    return np.array([sigma*(x[1]-x[0]),
                        x[0]*(rho-x[2])-x[1],
                        x[0]*x[1]-beta*x[2]])

def ensemble_plot(Ens,title=''):
    """
    Function to plot the locations of an ensemble of points.
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(Ens[:,0],Ens[:,1],Ens[:,2],'.')    
    pylab.title(title)

def ensemble(M,T):
    """
    Function to integrate an ensemble of trajectories of the Lorenz system.
    Inputs:
    M - the number of ensemble members
    T - the time to integrate for
    """
    ens = 0.1*np.random.randn(M,3)

    for m in range(M):
        t = np.array([0.,T])
        data = integrate.odeint(vectorfield, 
                                y0=ens[m,:], t=t, args=(10.0,28.,8./3.),
                                mxstep=100000)

        ens[m,:] = data[1,:]

    return ens

def f(d):
    """
    Function to apply ergodic average to.
    inputs:
    X - array, first dimension time, second dimension component
    outputs:
    f: - 1d- array of f values
    """

    return d[:,0]**2 + d[:,1]**2 + d[:,2]**2

def spatialaverage(f, M)

    return np.average(f(ens))

if __name__ == '__main__':

    Ens = ensemble(100, 0.5)
    ensemble_plot(Ens,'T=0.5')
    pylab.show()
