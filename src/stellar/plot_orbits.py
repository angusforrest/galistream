import argparse
import numpy
import math
import matplotlib.pyplot as plt
import pickle
import os
from multiprocessing.pool import Pool
from functools import partial

def animate_orbits(orbits):
    def generator_split(gen):
        cores = int(os.environ.get("OMP_NUM_THREADS"))
        if cores == 1:
            yield gen
        else:
            num = math.ceil(gen.size / cores - 1)
            for i in range(num):
                end = num*(i+1)
                if end > gen.size:
                    end = gen.size + 1
                yield gen[num*i:end]
                
    ts = orbits.t
    with Pool() as p:
        p.map(partial(plot_orbits,orbits),generator_split(ts))

def plot_orbits(orbits,ts):
    for t in ts:
        plot_orbit(orbits,t)

def plot_orbit(orbits,t):
    pyplot.ioff()
    ax = plt.axes()
    ax.set_aspect('equal', adjustable='box')
    xsys = [[orbit.x(t),orbit.y(t)] for orbit in orbits]
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_xlabel(f"x (kpc)")
    ax.set_ylabel(f"y (kpc)")
    ax.scatter(*zip(*xsys),s=1)
    plt.savefig(f"frame{t}.png",dpi=300)
    plt.close()
    
def main():

    if not ("OMP_NUM_THREADS" in os.environ):
        print("OMP_NUM_THREADS environmental variable not set")
        return 0

    parser = argparse.ArgumentParser("plot_orbits")
    parser.add_argument("filename")
    parser.add_argument("-a","--animation",default=True,type=bool)
    args = parser.parse_args()
    if os.path.exists(args.filename):
        with open(args.filename,"rb") as file:
            orbits = pickle.load(file)
    else:
        print("file provided does not exist")

    if args.animation == True:
        animate_orbits(orbits)
    else:
        print("non-animation plot not implemented yet")
        return 0

    return 0

if __name__ == '__main__':
    main()
