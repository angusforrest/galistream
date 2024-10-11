import argparse
import matplotlib.pyplot as plt
import numpy
import os
import pickle
import corner

def plot(data,res):
    plt.rcParams['text.usetex'] = True
    plt.ioff()
    l_ys = res[0][-1]
    energy = data[0,:,-1]
    momentum = data[1,:,-1]
    samples = numpy.array([(x,y-z) for x,y,z in zip(momentum,energy,l_ys)])
    figure = corner.corner(samples,labels=[r"$L_z$",r"\Delta E"],quantiles=[0.16,0.5,0.84], show_titles=True,title_kwargs={"fontsize": 12}) 
    plt.savefig("figure_corner.eps",dpi=600)
    plt.savefig("figure_corner.png",dpi=600)
    plt.close()
    
def main():
    parser = argparse.ArgumentParser("plot_corner")
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
            res = pickle.load(file)
    else:
        print("file provided does not exist")
        return 0
    plot(momentum,res)

if __name__ == "__main__":
    main()
