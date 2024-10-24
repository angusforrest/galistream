import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle

def plot(momentum,result):
    plt.rcParams['text.usetex'] = True
    plt.ioff()
    props = dict(boxstyle='round', facecolor='wheat', alpha=1)
    fig,ax = plt.subplots(1,1,figsize=(8,8))
    fig.set_tight_layout(True)
    lz = momentum[1,:,-1]
    energy = momentum[0,:,-1]
    ax.plot(sorted(lz),result[0][-1][numpy.argsort(lz)],color='orange')
    ax.scatter(lz,energy,s=1)
    ax.set_xlabel(r"Angular Momentum $L_z$ (kpc km s${}^{-1}$)")
    ax.set_ylabel(r"Total Energy $E$ (km${}^2$ s${}^{-2}$)")
    #ax[1].scatter(momentum[1,:,-1],momentum[0,:,-1]-result[0][-1],s=1)
    #ax[1].set_xlabel(r"$L_z$ (kpc km s${}^{-1}$)")
    #ax[1].set_ylabel(r"$\Delta E$ (km${}^2$ s${}^{-2}$)")
    plt.savefig("figure_scatter.png",dpi=600)
    plt.close()
    fig,ax = plt.subplots(1,2,figsize=(8,4),width_ratios=[3, 2])
    fig.set_tight_layout(True)
    lz = momentum[1,:,-1]
    energy = momentum[0,:,-1]
    residual = momentum[0,:,-1]-result[0][-1]
    ax[0].scatter(momentum[1,:,-1],residual,s=1)
    ax[0].set_xlabel(r"Angular Momentum $L_z$ (kpc km s${}^{-1}$)")
    ax[0].set_ylabel(r"Total Energy Residuals $\Delta E$ (km${}^2$ s${}^{-2}$)")
    ax[0].text(0.05, 0.95, 'A', transform=ax[0].transAxes, fontsize=10, fontweight='bold', va='bottom', ha='left')
    ax[1].hist(residual,35,orientation='horizontal')
    ax[1].text(0.05, 0.95, 'B', transform=ax[1].transAxes, fontsize=10, fontweight='bold', va='bottom', ha='left')

    per84 = numpy.percentile(residual,84.0)
    per16 = numpy.percentile(residual,16.0)
    per50 = numpy.percentile(residual,50.0)

    ax[1].axhline(per84,color="orange",linestyle="dashed")
    ax[1].axhline(per16,color="orange",linestyle="dashed")
    ax[1].axhline(per50,color="orange",linestyle="dashed")
    ax[1].set_yticks([])
    ax[1].set_xticks([])
    pertext=f"84th percentile {per84:2.1f}\n50th percentile {per50:2.1f}\n16th percentile {per16:2.1f}"
    ax[1].text(0.95, 0.95, pertext, transform=ax[1].transAxes, fontsize=10, va='top', ha='right')
    plt.savefig("figure_histogram.png",dpi=600)
    plt.close()
    fig,ax = plt.subplots(1,1,figsize=(8,4.5))
    fig.set_tight_layout(True)
    ax.scatter(momentum[1,:,12],momentum[0,:,12],s=1)
    ax.scatter(momentum[1,:,20]+100,momentum[0,:,20],s=1)
    ax.scatter(momentum[1,:,33]+200,momentum[0,:,33],s=1)
    ax.text(0.05, 0.95, 'A', transform=ax.transAxes, fontsize=20, fontweight='bold', va='top', ha='right')
    ax.text(0.35, 0.95, 'B', transform=ax.transAxes, fontsize=20, fontweight='bold', va='top', ha='right')
    ax.text(0.70, 0.95, 'C', transform=ax.transAxes, fontsize=20, fontweight='bold', va='top', ha='right')
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlabel(r"Angular Momentum $L_z$ (kpc km s${}^{-1}$)")
    ax.set_ylabel(r"Total Energy $E$ (km${}^2$ s${}^{-2}$)")
    plt.savefig("figure_discussion2.png",dpi=600)
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
