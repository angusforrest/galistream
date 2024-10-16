import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle

def plot(momentum,result):
    plt.rcParams['text.usetex'] = True
    plt.ioff()
    props = dict(boxstyle='round', facecolor='wheat', alpha=1)
    fig,axs = plt.subplots(3,2,figsize=(8,10))
    fig.set_tight_layout(True)
    ts = [12,16,20,25,33,39]
    labels = ['A','B','C','D','E','F']
    for ax in axs.flatten():
        residual = momentum[0,:,ts[i]] - result[0][ts[i]]        
        ax.hist(residual,35,orientation='vertical')
        ax.text(0.05, 0.95, labels[i], transform=ax[1].transAxes, fontsize=10, fontweight='bold', va='bottom', ha='left')

        per84 = numpy.percentile(residual,84.0)
        per16 = numpy.percentile(residual,16.0)
        per50 = numpy.percentile(residual,50.0)

        ax.axvline(per84,color="orange",linestyle="dashed")
        ax.axvline(per16,color="orange",linestyle="dashed")
        ax.axvline(per50,color="orange",linestyle="dashed")
        ax.set_yticks([])
        ax.set_xticks([])
        pertext=f"84th percentile {per84:2.1f}\n50th percentile {per50:2.1f}\n16th percentile {per16:2.1f}"
        ax.text(0.95, 0.95, pertext, transform=ax[1].transAxes, fontsize=10, va='top', ha='right')

    plt.subplots_adjust(wspace=0, hspace=0)
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
