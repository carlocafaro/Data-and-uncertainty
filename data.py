from scipy import integrate
import numpy as np
import pylab

"""
File containing code relating to Computational Lab 1 of the Dynamics
MPECDT core course.

You should fork this repository and add any extra functions and
classes to this module.
"""

def vectorfield(x, t, alpha, beta):
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

    return alpha*x + beta

def getdata(y0,T,Deltat):
    """
    Function to return simulated observational data from a dynamical
    system, for testing out forecasting tools with.

    Inputs:
    y0 - the initial condition of the system state
    T - The final time to simulate until
    Deltat - the time intervals to obtain observations from. Note
    that the numerical integration method is time-adaptive and
    chooses it's own timestep size, but will interpolate to obtain
    values at these intervals.
    """
    t = np.arange(0.,T,Deltat)
    data = integrate.odeint(vectorfield, y0, t=t, args=(1.0,0.1))
    return data, t

def plot3D(x,y,z):
    """
    Make a 3D plot of data.
    Inputs:
    x - Numpy array of x coordinate
    y - Numpy array of y coordinate
    z - Numpy array of z coordinate
    """
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x,y,z)
    pylab.show()
            
if __name__ == '__main__':
    mydat, mytime = getdata(1.1,10.0,1.0)

    pylab.plot(mytime,mydat)
    pylab.show()
