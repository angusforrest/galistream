import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle

def plot(momentum,result):
    plt.rcParams['text.usetex'] = True
    plt.ioff()
    props = dict(boxstyle='round', facecolor='wheat', alpha=1)
    fig,ax = plt.subplots(1,2)
    ax[0,0].scatter(momentum[1,:,-1],momentum[0,:,-1])
    ax[0,0].set_xlabel(r"$L_z$ (kpc km s${}^{-1}$)")
    ax[0,0].set_ylabel(r"$\Delta E$ (km^2 s${}^{-2}$)")
    ax[0,1].scatter(momentum[1,:,-1],momentum[0,:,-1]-result[0][-1])
    ax[0,1].set_xlabel(r"$L_z$ (kpc km s${}^{-1}$)")
    ax[0,1].set_ylabel(r"$\Delta E$ (km^2 s${}^{-2}$)")
    plt.savefig("figure_scatter.eps",dpi=300)
    plt.savefig("figure_scatter.png",dpi=300)
    plt.close()


def main():
    parser = argparse.ArgumentParser("plot_scatter")
    parser.add_argument("momentum")
    parser.add_argument("result")
    args = parser.parse_args()
    if os.path.exists(args.gmc_orbits):
        with open(args.gmc_orbits,"rb") as file:
            orbits = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.gmc_orbits):
        with open(args.gmc_orbits,"rb") as file:
            orbits = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0

    plot(orbits)

if __name__ == "__main__":
    main()
