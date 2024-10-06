import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle

def plot(orbits):
    ts = orbits.t
    plt.ioff()
    fig,ax = plt.subplots(2,2,sharex=True,sharey=True)
    # 0 Gyr GMC Plot
    ax[0,0].scatter(orbits.x(0),orbits.y(0),s=1)
    ax[0,0].set_xlim(-10,10)
    ax[0,0].set_ylim(-10,10)
    ax[0,0].set_ylabel(f"y (kpc)")
    ax[0,0].set_aspect('equal')
    # 1 Gyr GMC Plot
    ax[0,1].scatter(orbits.x(ts[-1]),orbits.y(ts[-1]),s=1)
    ax[0,1].set_xlim(-10,10)
    ax[0,1].set_ylim(-10,10)
    ax[0,1].set_ylabel(f"y (kpc)")
    ax[0,1].set_aspect('equal')
    # 0 Gyr Colormap GMC Plot
    im = ax[1,0].scatter(orbits.x(0),orbits.y(0),c=orbits.phi(0),cmap="ocean",s=1)
    fig.colorbar(im,ax=ax[1,0])
    ax[1,0].set_xlim(-10,10)
    ax[1,0].set_ylim(-10,10)
    ax[1,0].set_xlabel(f"x (kpc)")
    ax[1,0].set_aspect('equal')
    # 1 Gyr Colormap GMC Plot
    im = ax[1,1].scatter(orbits.x(ts[-1]),orbits.y(ts[-1]),c=orbits.phi(ts[-1]),cmap="ocean",s=1)
    fig.colorbar(im,ax=ax[1,1])
    ax[1,1].set_xlim(-10,10)
    ax[1,1].set_ylim(-10,10)
    ax[1,1].set_xlabel(f"x (kpc)")
    ax[1,1].set_aspect('equal')
    plt.savefig("figure_gmc_angular.eps",dpi=600)
    plt.savefig("figure_gmc_angular.png",dpi=600)
    plt.close()


def main():
    parser = argparse.ArgumentParser("plot_gmc_angular")
    parser.add_argument("gmc_orbits")
    args = parser.parse_args()
    if os.path.exists(args.gmc_orbits):
        with open(args.gmc_orbits,"rb") as file:
            orbits = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0

    plot(orbits)

if __name__ == "__main__":
    main()
