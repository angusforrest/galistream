import argparse
import matplotlib
import numpy
import os
import pickle

def plot(orbits):
    ts = orbits.t
    plt.ioff()
    fig,ax = plt.subplots(2,2,sharex=True)
    # 0 Gyr GMC Plot
    ax[0,0].scatter(orbits.x(0),orbits.y(0),)
    ax[0,0].set_limx(-10,10)
    ax[0,0].set_limy(-10,10)
    ax[0,0].set_xlabel(f"x (kpc)")
    ax[0,0].set_xlabel(f"y (kpc)")
    ax[0,0].set_aspect('equal')
    # 1 Gyr GMC Plot
    ax[1,0].scatter(orbits.x(ts[-1]),orbits.y(ts[-1]))
    ax[1,0].set_limx(-10,10)
    ax[1,0].set_limy(-10,10)
    ax[1,0].set_xlabel(f"x (kpc)")
    ax[1,0].set_xlabel(f"y (kpc)")
    ax[1,0].set_aspect('equal')
    # 0 Gyr Colormap GMC Plot
    ax[0,1].scatter(orbits.x(0),orbits.y(0),c=orbits.theta(0),cmap=ocean)
    ax[0,1].colorbar()
    ax[0,1].set_limx(-10,10)
    ax[0,1].set_limy(-10,10)
    ax[0,1].set_xlabel(f"x (kpc)")
    ax[0,1].set_xlabel(f"y (kpc)")
    ax[0,1].set_aspect('equal')
    # 1 Gyr Colormap GMC Plot
    ax[1,1].scatter(orbits.x(ts[-1]),orbits.y(ts[-1]),c=orbits.theta(ts[-1]),cmap=ocean)
    ax[1,1].colorbar()
    ax[1,1].set_limx(-10,10)
    ax[1,1].set_limy(-10,10)
    ax[1,1].set_xlabel(f"x (kpc)")
    ax[1,1].set_xlabel(f"y (kpc)")
    ax[1,1].set_aspect('equal')
    plt.savefig("figure_gmc_angular.eps",dpi=600)
    plt.close()


def main():
    parser = argparse.ArugmentParser("plot_gmc_angular")
    parser.add_argument("gmc_orbits")
    if os.path.exists(args.gmc_orbits):
        with open(args.gmc_orbits,"rb") as file:
            orbits = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0

    plot(orbits)

if __name__ == "__main__":
    main()
