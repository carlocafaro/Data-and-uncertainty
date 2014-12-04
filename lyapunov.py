import numpy as np
import pylab

def linear_lorenz_vectorfield(y,t,sigma,rho,beta):
    """
    Function to integrate the lorenz equations together
    with the linearised equations about that trajectory.
    
    inputs:
    y - array containing (x,y,z,dx,dy,dz)
    t - time, not used but needed for the interface
    rho, sigma,beta - parameters
    """

    x = y[:3]
    dx = y[3:]

    #This needs changing
    xdot = np.array([1.,2.,3.])
    dxdot = np.array([4.,5.,6.])

    #combine xdot and dxdot into one field
    return np.concatenate((xdot,dxdot))

def Phi(x,dx,T):
    """
    Function to integrate the linearised Lorenz equations about
    a given trajectory.
    Inputs:
    x - the initial conditions for the Lorenz trajectory
    dx - the initial conditions for the perturbation
    T - the length of time to integrate for

    Outputs:
    dx - the final value of the perturbation
    """

    y0 = np.concatenate((x,dx))
    t = np.array([0.,T])
    data = integrate.odeint(linear_lorenz_vectorfield, y0, t=t, args=(10.,28.,8./3.))
    
    return data[1,3:]
