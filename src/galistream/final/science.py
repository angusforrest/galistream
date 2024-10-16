import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle

def plot(d0_0,d1250_0,d1250_1,d1250_2,d2500_0,d2500_1,d2500_2,d5000_0,d5000_1):
    COL3 = '#FFBA08'
    COL2 = '#F48C06'
    COL1 = '#DC2F02'
    COL0 = '#9D0208'
    COLWHITE = '#F7F7F8'
    COLBLACK = '#001134'
    plt.rcParams['text.usetex'] = True
    plt.ioff()
    fig,ax = plt.subplots(2,1,figsize=(8,10),sharex=True)
    fig.set_tight_layout(True)
    ts = d1250_0[-1]
    ax[0].plot(ts,d0_0[1],c=COL0,label="0",linestyle="dashed")
    ax[0].plot(ts,d1250_0[1],c=COL1,label="1250")
    ax[0].plot(ts,d1250_1[1],c=COL1)
    ax[0].plot(ts,d1250_2[1],c=COL1)
    ax[0].plot(ts,d2500_0[1],c=COL2,label="2500")
    ax[0].plot(ts,d2500_1[1],c=COL2)
    ax[0].plot(ts,d2500_2[1],c=COL2)
    ax[0].plot(ts,d5000_0[1],c=COL3,label="5000")
    ax[0].plot(ts,d5000_1[1],c=COL3)
    ax[0].legend(loc="upper left")
    ax[0].set_ylabel(r'$\Delta E$ km${}^{2}$ s$^{-2}$')
    ax[0].set_xlim(0,1)
    ax[0].legend(fontsize=20,loc="upper left",title="no. GMCs")
    bbox = dict(boxstyle='round', fc='blanchedalmond', ec='orange', alpha=1)
    ax[1].axvline(ts[12],0,0.95,linestyle='dashed')
    ax[1].text(ts[12],6.5,"A",bbox=bbox,horizontalalignment='center')
    ax[1].axvline(ts[16],0,0.95,linestyle='dashed')
    ax[1].text(ts[16],6.5,"B",bbox=bbox,horizontalalignment='center')
    ax[1].axvline(ts[20],0,0.95,linestyle='dashed')
    ax[1].text(ts[20],6.5,"C",bbox=bbox,horizontalalignment='center')
    ax[1].axvline(ts[25],0,0.95,linestyle='dashed')
    ax[1].text(ts[25],6.5,"D",bbox=bbox,horizontalalignment='center')
    ax[1].axvline(ts[33],0,0.95,linestyle='dashed')
    ax[1].text(ts[33],6.5,"E",bbox=bbox,horizontalalignment='center')
    ax[1].axvline(ts[39],0,0.95,linestyle='dashed')
    ax[1].text(ts[39],6.5,"F",bbox=bbox,horizontalalignment='center')
    ax[1].plot(ts,numpy.sqrt(d0_0[1]),c=COL0,label="0",linestyle="dashed")
    ax[1].plot(ts,numpy.sqrt(d1250_0[1]),c=COL1,label="1250")
    ax[1].plot(ts,numpy.sqrt(d1250_1[1]),c=COL1)
    ax[1].plot(ts,numpy.sqrt(d1250_2[1]),c=COL1)
    ax[1].plot(ts,numpy.sqrt(d2500_0[1]),c=COL2,label="2500")
    ax[1].plot(ts,numpy.sqrt(d2500_1[1]),c=COL2)
    ax[1].plot(ts,numpy.sqrt(d2500_2[1]),c=COL2)
    ax[1].plot(ts,numpy.sqrt(d5000_0[1]),c=COL3,label="5000")
    ax[1].plot(ts,numpy.sqrt(d5000_1[1]),c=COL3)
    ax[1].legend(loc="upper left")
    ax[1].legend(loc="upper left",title="no. GMCs")
    ax[1].set_xlabel("time (Gyr)")
    ax[1].set_ylabel(r'$\sigma$ km s$({}^{-1})$')
    ax[1].set_xlim(0,1)
    plt.savefig("figure_sigma.png",dpi=600)
    plt.close()

def main():
    parser = argparse.ArgumentParser("plot_gmc_angular")
    parser.add_argument("d0_0")
    parser.add_argument("d1250_0")
    parser.add_argument("d1250_1")
    parser.add_argument("d1250_2")
    parser.add_argument("d2500_0")
    parser.add_argument("d2500_1")
    parser.add_argument("d2500_2")
    parser.add_argument("d5000_0")
    parser.add_argument("d5000_1")
    args = parser.parse_args()
    if os.path.exists(args.d0_0):
        with open(args.d0_0,"rb") as file:
            d0_0 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d1250_0):
        with open(args.d1250_0,"rb") as file:
            d1250_0 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d1250_1):
        with open(args.d1250_1,"rb") as file:
            d1250_1 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d1250_2):
        with open(args.d1250_2,"rb") as file:
            d1250_2 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d2500_0):
        with open(args.d2500_0,"rb") as file:
            d2500_0 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d2500_1):
        with open(args.d2500_1,"rb") as file:
            d2500_1 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d2500_2):
        with open(args.d2500_2,"rb") as file:
            d2500_2 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d5000_0):
        with open(args.d5000_0,"rb") as file:
            d5000_0 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    if os.path.exists(args.d5000_1):
        with open(args.d5000_1,"rb") as file:
            d5000_1 = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    plot(d0_0,d1250_0,d1250_1,d1250_2,d2500_0,d2500_1,d2500_2,d5000_0,d5000_1)

if __name__ == "__main__":
    main()
