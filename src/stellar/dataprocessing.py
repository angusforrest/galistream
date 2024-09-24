import argparse
import numpy
import matplotlib.pyplot as plt
import pickle
import os
from loess import loess_1d

def bootstrap(data):
    sigmas = []
    for j in range(1000):
        n_resamples = 10000
        bootstrap = [data[:,numpy.random.randint(len(data.shape[1]))] for n in range(n_resamples)]
        sigmas.append(loess_curve(data))
    per16 = numpy.percentile(sigmas, 16.0)
    per84 = numpy.percentile(sigmas, 84.0)
    return (per16,per84)



def data_process(data):
    for i in data.shape[2]:
        sigma = loess_curve(data[0,:,i],data[1,:,i])
        bootstrap_sigmas = bootstrap(data[:,:,i])
        
def loess_curve(xs,ys):
    l_xs, l_ys, out = loess_1d(data[0,:,i],data[1,:,i], xnew=None, degree=1,frac=0.5,npoints=None,rotate=False,sigy=None)
    new_data = numpy.array([(x,y-z) for x,y,z in zip(xs,ys,l_ys)])
    per16 = numpy.percentile(new_data[1,:],16.0)
    per84 = numpy.percentile(new_data[1,:],84.0)
    sigma = (per84-per16)/2
    return sigma

def main():
    data_process(data)
    
    return 0

if __name__ == '__main__':
    main()
