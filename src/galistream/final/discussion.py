import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle

def plot(momentum,result):
    plt.rcParams['agg.path.chunksize'] = 100000
    plt.rcParams['text.usetex'] = True
    plt.ioff()
    props = dict(boxstyle='round', facecolor='wheat', alpha=1)
    fig,ax = plt.subplots(2,3,figsize=(18,10),sharex=True,sharey=True)
    fig.set_tight_layout(True)
    lz = momentum[1,:,12]
    energy = momentum[0,:,12]
    ax[0,0].plot(sorted(lz),result[0][12][numpy.argsort(lz)],color='orange')
    ax[0,0].scatter(lz,energy,s=1)
    ax[0,0].set_ylabel(r"$\Delta E$ (km${}^2$ s${}^{-2}$)")
    lz = momentum[1,:,16]
    energy = momentum[0,:,16]
    ax[0,1].plot(sorted(lz),result[0][16][numpy.argsort(lz)],color='orange')
    ax[0,1].scatter(lz,energy,s=1)
    lz = momentum[1,:,20]
    energy = momentum[0,:,20]
    ax[0,2].plot(sorted(lz),result[0][20][numpy.argsort(lz)],color='orange')
    ax[0,2].scatter(lz,energy,s=1)
    lz = momentum[1,:,25]
    energy = momentum[0,:,25]
    ax[1,0].plot(sorted(lz),result[0][25][numpy.argsort(lz)],color='orange')
    ax[1,0].scatter(lz,energy,s=1)
    ax[1,0].set_xlabel(r"$L_z$ (kpc km s${}^{-1}$)")
    ax[1,0].set_ylabel(r"$\Delta E$ (km${}^2$ s${}^{-2}$)")
    lz = momentum[1,:,33]
    energy = momentum[0,:,33]
    ax[1,1].plot(sorted(lz),result[0][33][numpy.argsort(lz)],color='orange')
    ax[1,1].scatter(lz,energy,s=1)
    ax[1,1].set_xlabel(r"$L_z$ (kpc km s${}^{-1}$)")
    lz = momentum[1,:,39]
    energy = momentum[0,:,39]
    ax[1,2].plot(sorted(lz),result[0][39][numpy.argsort(lz)],color='orange')
    ax[1,2].scatter(lz,energy,s=1)
    ax[1,2].set_xlabel(r"$L_z$ (kpc km s${}^{-1}$)")
    plt.savefig("figure_discussion.eps",dpi=600)
    plt.savefig("figure_discussion.png",dpi=600)
    plt.close()


def main():
    parser = argparse.ArgumentParser("plot_scatter")
    parser.add_argument("momentum")
    parser.add_argument("result")
    args = parser.parse_args()
    if os.path.exists(args.momentum):
        with open(args.momentum,"rb") as file:
            momentum = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.result):
        with open(args.result,"rb") as file:
            result = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0

    plot(momentum,result)

if __name__ == "__main__":
    main()
