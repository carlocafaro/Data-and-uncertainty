import numpy as np
import pylab as pl


def square(x):
   """
   Function to compute the square of the input. If the input is
   a numpy array, this returns a numpy array of all of the squared values.
   inputs:
   x - a numpy array of values

   outputs:
   y - a numpy array containing the square of all of the values
   """
   return x**2

def normal(N):
   """
   Function to return a numpy array containing N samples from
   a N(0,1) distribution.
   """
   return np.random.randn(N)

def montecarlo(f, X, N):
   """
   Function to compute the Monte Carlo estimate of the expectation
   E[f(X)], with N samples

   inputs:
   f - a Python function that applies a chosen mathematical function to
   each entry in a numpy array
   X - a Python function that takes N as input and returns
   independent individually distributed random samples from a chosen
   probability distribution
   N - the number of samples to use
   """

   theta = np.sum(f(X(N)))/N
   error_estimate = np.sum(f(X(N))-theta)**2/(N-1)
   return theta, error_estimate

if __name__ == '__main__':    
   
   
    Ns=np.array([10,100,1000,10000,100000,1000000,10000000])
    err=np.zeros(Ns.shape)
    
    for i,N in enumerate(Ns):
	theta, error_estimate = montecarlo(square,normal,N)
        err[i]=np.abs(1.0 - theta)
        err_estim[i]=error_estimate
   
        print 
        
    pl.clf()
    pl.loglog(Ns, err,   'k',   label='true error')
    pl.loglog(Ns, err_estim, 'r'  ,label='estimate error') 
    
    #plt.xlim([0, 2**14]) # <--- this line does nothing
    pl.show()
    
    

