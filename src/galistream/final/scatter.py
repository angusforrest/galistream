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
    fig,ax = plt.subplots(1,1,figsize=(8,8))
    fig.set_tight_layout(True)
    lz = momentum[1,:,-1]
    energy = momentum[0,:,-1]
    ax.plot(sorted(lz),result[0][-1][numpy.argsort(lz)],color='orange')
    ax.scatter(lz,energy,s=1)
    ax.set_xlabel(r"$L_z$ (kpc km s${}^{-1}$)")
    ax.set_ylabel(r"$\Delta E$ (km${}^2$ s${}^{-2}$)")
    #ax[1].scatter(momentum[1,:,-1],momentum[0,:,-1]-result[0][-1],s=1)
    #ax[1].set_xlabel(r"$L_z$ (kpc km s${}^{-1}$)")
    #ax[1].set_ylabel(r"$\Delta E$ (km${}^2$ s${}^{-2}$)")
    plt.savefig("figure_scatter.png",dpi=600)
    plt.close()
    fig,ax = plt.subplots(1,2,figsize=(8,4))
    fig.set_tight_layout(True)
    lz = momentum[1,:,-1]
    energy = momentum[0,:,-1]
    residual = momentum[0,:,-1]-result[0][-1]
    ax[0].scatter(momentum[1,:,-1],residual,s=1)
    ax[0].set_xlabel(r"$L_z$ (kpc km s${}^{-1}$)")
    ax[0].set_ylabel(r"$\Delta E$ (km${}^2$ s${}^{-2}$)")
    ax[1].hist(residual,orientation='horizontal')
    ax[1].axhline(numpy.percentile(residual,86.0))
    ax[1].axhline(numpy.percentile(residual,14.0))
    ax[1].axhline(numpy.percentile(residual,50.0))
    ax[1].set_yticks([])
    ax[1].set_xticks([])
    plt.savefig("figure_histogram.png",dpi=600)
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
