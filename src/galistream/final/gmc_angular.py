import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle

def plot(orbits):
    ts = orbits.t
    plt.ioff()
    props = dict(boxstyle='round', facecolor='wheat', alpha=1)
    fig,ax = plt.subplots(2,2,sharex=True,sharey=True)
    fig.set_tight_layout(True)
    # 0 Gyr GMC Plot
    ax[0,0].scatter(orbits.x(0),orbits.y(0),s=.1)
    ax[0,0].set_xlim(-10,10)
    ax[0,0].set_ylim(-10,10)
    ax[0,0].set_ylabel(f"y (kpc)")
    ax[0,0].set_aspect('equal')
    ax[0,0].text(0.05, 0.95, r't = 0 Gyr', transform=ax[0,0].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)
    # 1 Gyr GMC Plot
    ax[1,0].scatter(orbits.x(ts[-1]),orbits.y(ts[-1]),s=.1)
    ax[1,0].set_xlim(-10,10)
    ax[1,0].set_ylim(-10,10)
    ax[1,0].set_ylabel(f"y (kpc)")
    ax[1,0].set_xlabel(f"x (kpc)")
    ax[1,0].set_aspect('equal')
    ax[1,0].text(0.05, 0.95, r't = 1 Gyr', transform=ax[1,0].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)
    # 0 Gyr Colormap GMC Plot
    im = ax[0,1].scatter(orbits.x(0),orbits.y(0),c=orbits.phi(0),cmap="twilight",s=1)
    phi = sorted(orbits.phi(0))
    print(phi[0],phi[-1])
    cbar = fig.colorbar(im,ax=ax[0,1],ticks=[phi[0], 0, phi[-1]])
    cbar.ax.set_yticklabels([r'-180', '0', r'180'])
    ax[0,1].set_xlim(-10,10)
    ax[0,1].set_ylim(-10,10)
    ax[0,1].set_aspect('equal')
    ax[0,1].text(0.05, 0.95, r't = 0 Gyr', transform=ax[0,1].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)
    # 1 Gyr Colormap GMC Plot
    im = ax[1,1].scatter(orbits.x(ts[-1]),orbits.y(ts[-1]),c=orbits.phi(0),cmap="twilight",s=1)
    cbar = fig.colorbar(im,ax=ax[1,1],ticks=[-numpy.pi, 0, numpy.pi])
    labels = cbar.ax.get_yticklabels()
    labels[0].set_verticalalignment('top')
    labels[-1].set_verticalalignment('bottom')
    cbar.ax.set_yticklabels([r'-180', '0', r'180'])
    ax[1,1].set_xlim(-10,10)
    ax[1,1].set_ylim(-10,10)
    ax[1,1].set_xlabel(f"x (kpc)")
    ax[1,1].set_aspect('equal')
    ax[1,1].text(0.05, 0.95, r't = 1 Gyr', transform=ax[1,1].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)
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
