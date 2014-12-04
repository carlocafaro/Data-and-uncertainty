import pylab
import numpy as np

def Vprime_bistable(x):
    return x**3-x

def brownian_dynamics(x,Vp,sigma,dt,T,tdump):
    """
    Solve the Brownian dynamics equation

    dx = -V(x)dt + sigma*dW

    using the Euler-Maruyama method

    x^{n+1} = x^n - V(x^n)dt + sigma*dW

    inputs:
    x - initial condition for x
    Vp - a function that returns V'(x) given x
    dt - the time stepsize
    T - the time limit for the simulation
    tdump - the time interval between storing values of x

    outputs:
    xvals - a numpy array containing the values of x at the chosen time points
    tvals - a numpy array containing the values of t at the same points
    """

    xvals = [x]
    t = 0.
    tvals = [0]
    dumpt = 0.
    while(t<T-0.5*dt):
        dW = dt**0.5*np.random.randn()
        x += -Vp(x)*dt + sigma*dW

        t += dt
        dumpt += dt

        if(dumpt>tdump-0.5*dt):
            dumpt -= tdump
            xvals.append(x)
            tvals.append(t)
    return np.array(xvals), np.array(tvals)

if __name__ == '__main__':
    dt = 0.1
    sigma =0.25
    T = 1000.0
    x,t = brownian_dynamics(0.0,Vprime_bistable,sigma,dt,T,dt)
    pylab.plot(t,x)

    pylab.show()

