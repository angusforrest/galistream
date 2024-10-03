import argparse
import numpy
import matplotlib.pyplot as plt
import pickle
import os
from loess.loess_1d import loess_1d

def loess_curve(xs,ys):
    l_xs, l_ys, out = loess_1d(xs,ys, xnew=None, degree=1,frac=0.5,npoints=None,rotate=False,sigy=None)
    new_data = numpy.array([(x,y-z) for x,y,z in zip(xs,ys,l_ys)])
    per16 = numpy.percentile(new_data[:,1],16.0)
    per84 = numpy.percentile(new_data[:,1],84.0)
    sigma = (per84-per16)/2
    lower, upper = bootstrap(new_data)
    return (l_ys,sigma,lower,upper)

def bootstrap(data):
    sigmas = []
    for j in range(50):
        n_resamples = 10000
        boot = numpy.array([data[:,numpy.random.randint(data.shape[1])] for n in range(n_resamples)])
        per16 = numpy.percentile(new_data[:,1],16.0)
        per84 = numpy.percentile(new_data[:,1],84.0)
        sigmas.append((per84-per16)/2)
    lower = numpy.percentile(sigmas, 16.0)
    upper = numpy.percentile(sigmas, 84.0)
    return (lower,upper)


def data_process(data):
    output = []
    loess = []
    y1 = []
    y2 = []
    ts = numpy.arange(0,2001,40) * (1/2001)
    for i in range(data.shape[2]):
        # input1 = Lz input2 = E
        l_ys,sigma,lower,upper = loess_curve(data[1,:,i],data[0,:,i])
        loess.append(l_ys)
        output.append(sigma)
        y1.append(lower)
        y2.append(upper)
    savedata = (loess,output,y1,y2,ts)
    with open("results.pickle","wb") as file:
        pickle.dump(savedata,file)
    ax = plt.axes()
    ax.fill_between(ts,lower,upper)
    ax.plot(ts,output)
    ax.set_title(r"$t$ versus $\sigma^2=\Delta E$")
    plt.savefig("sigma_graph.png",dpi=600)
    plt.close()
    ax = plt.axes()
    ax.fill_between(ts,numpy.sqrt(lower),numpy.sqrt(upper))
    ax.plot(ts,numpy.sqrt(output))
    ax.set_title(r"$t$ versus $\sigma=\sqrt{\Delta E}$")
    plt.savefig("sigma2_graph.png",dpi=600)
    plt.close()
    return 0


def main():
	parser = argparse.ArgumentParser("dataprocessing")
	parser.add_argument("filename")
	args =parser.parse_args()
	if os.path.exists(args.filename):
		with open(args.filename, "rb") as file:
			data = pickle.load(file)
	else:
		print("file provided does not exist")
		return 0
	data_process(data)
	return 0

if __name__ == '__main__':
    main()
