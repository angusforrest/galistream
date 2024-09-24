import argparse
import loess
import numpy
import matplotlib.pyplot as plt
import pickle
import os


def loess_curve(data):
    for i in data.shape[2]:
    xs, ys, out = loess_1d(data[0,:,i],data[1,:,i], xnew=None, degree=1,frac=0.5,npoints=None,rotate=False,sigy=None)
    new_data = [(x,y-z) for x,y,z in zip(data[0,:,i],data[1,:,i],ys)]
    per16 = numpy.percentile(new_data,16.0)
    per84 = numpy.percentile(new_data,84.0)
    sigma = (per84-per16)/2

def main():
    loess_curve(data)
    return 0

if __name__ == '__main__':
    main()
