import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle

def plot(d1250_0,d1250_1,d1250_2,d2500_0,d2500_1,d2500_2,d5000_0,d5000_1):
    plt.rcParams['text.usetex'] = True
    plt.ioff()
    fig,ax = plt.subplots()
    ts = d1250_0[-1]
    ax.plot(ts,d1250_0[1],c="blue",label="1250")
    ax.plot(ts,d1250_1[1],c="blue")
    ax.plot(ts,d1250_2[1],c="blue")
    ax.plot(ts,d2500_0[1],c="green",label="2500")
    ax.plot(ts,d2500_1[1],c="green")
    ax.plot(ts,d2500_2[1],c="green")
    ax.plot(ts,d5000_0[1],c="red",label="5000")
    ax.plot(ts,d5000_1[1],c="red")
    ax.legend(loc="upper left")
    ax.set_xlabel("time (Gyr)")
    ax.set_ylabel(r'$\sigma^2 = \Delta E$')
    plt.savefig("figure_sigma2.eps",dpi=600)
    plt.savefig("figure_sigma2.png",dpi=600)
    plt.close()
    fig,ax = plt.subplots()
    ts = d1250_0[-1]
    ax.plot(ts,numpy.sqrt(d1250_0[1]),c="blue",label="1250")
    ax.plot(ts,numpy.sqrt(d1250_1[1]),c="blue")
    ax.plot(ts,numpy.sqrt(d1250_2[1]),c="blue")
    ax.plot(ts,numpy.sqrt(d2500_0[1]),c="green",label="2500")
    ax.plot(ts,numpy.sqrt(d2500_1[1]),c="green")
    ax.plot(ts,numpy.sqrt(d2500_2[1]),c="green")
    ax.plot(ts,numpy.sqrt(d5000_0[1]),c="red",label="5000")
    ax.plot(ts,numpy.sqrt(d5000_1[1]),c="red")
    ax.legend(loc="upper left")
    ax.set_xlabel("time (Gyr)")
    ax.set_ylabel(r'$\sigma = \sqrt{\Delta E}$')
    plt.savefig("figure_sigma.eps",dpi=600)
    plt.savefig("figure_sigma.png",dpi=600)
    plt.close()

def main():
    parser = argparse.ArgumentParser("plot_gmc_angular")
    #parser.add_argument("d0_0")
    parser.add_argument("d1250_0")
    parser.add_argument("d1250_1")
    parser.add_argument("d1250_2")
    parser.add_argument("d2500_0")
    parser.add_argument("d2500_1")
    parser.add_argument("d2500_2")
    parser.add_argument("d5000_0")
    parser.add_argument("d5000_1")
    args = parser.parse_args()
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
    plot(d1250_0,d1250_1,d1250_2,d2500_0,d2500_1,d2500_2,d5000_0,d5000_1)

if __name__ == "__main__":
    main()
