import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle

def plot(data):
    energy = data[0,:,-1]
    momentum = data[1,:,-1]
    plt.rcParams['text.usetex'] = True
    plt.rcParams.update({'font.size': 48})
    plt.rcParams['lines.linewidth'] = 8
    plt.ioff()
    fig,ax = plt.subplots(figsize=(16.5,12.3))
    fig.set_tight_layout(True)
    ax.scatter(momentum,energy)
    ax.spines[['right', 'top']].set_visible(False)
    ax.set_xlabel(r"z axis angular momentum  $L_z$ (km kpc/s)")
    ax.set_ylabel(r'total energy $E$ (km${}^2$/s${}^2$)')
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(8)
    ax.tick_params(width=8)
    plt.savefig("figure_momentum.svg",dpi=600,transparent=True)
    plt.savefig("figure_momentum.png",dpi=600,transparent=True)
    plt.close()

def main():
    parser = argparse.ArgumentParser("plot_momentum")
    parser.add_argument("data")
    args = parser.parse_args()
    if os.path.exists(args.data):
        with open(args.data,"rb") as file:
            data = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    plot(data)

if __name__ == "__main__":
    main()
