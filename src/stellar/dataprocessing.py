import argparse
import numpy
import matplotlib.pyplot as plt
import pickle
import os
from loess import loess_1d

def loess_curve(xs,ys):
    l_xs, l_ys, out = loess_1d(data[0,:,i],data[1,:,i], xnew=None, degree=1,frac=0.5,npoints=None,rotate=False,sigy=None)
    new_data = numpy.array([(x,y-z) for x,y,z in zip(xs,ys,l_ys)])
    per16 = numpy.percentile(new_data[1,:],16.0)
    per84 = numpy.percentile(new_data[1,:],84.0)
    sigma = (per84-per16)/2
    return sigma

def bootstrap(data):
    sigmas = []
    for j in range(1000):
        n_resamples = 10000
        bootstrap = [data[:,numpy.random.randint(len(data.shape[1]))] for n in range(n_resamples)]
        sigmas.append(loess_curve(data))
    per16 = numpy.percentile(sigmas, 16.0)
    per84 = numpy.percentile(sigmas, 84.0)
    return (per16,per84)

class Output:
    def __init__(self, data,y1,y2,ts):
        self.data = data
        self.y1 = y1
        self.y2 = y2
        self.ts = ts
    

def data_process(data):
    output = []
    y1 = []
    y2 = []
    ts = numpy.linspace(0,1,data.shape[2])
    for i in range(data.shape[2]):
        sigma = loess_curve(data[0,:,i],data[1,:,i])
        x1,x2 = bootstrap(data[:,:,i])
        output.append(sigma)
        y1.append(x1)
        y2.append(x2)
    savedata = Output(output,y1,y2,ts)
    with open("results.pickle","wb") as file:
        pickle.dump(savedata,file)
    ax = plt.axes()
    ax.fill_between(ts,y1,y2)
    ax.plot(ts,output)
    ax.set_title(r"$t$ versus $\sigma$")
    plt.savefig("graph.png",dpi=600)


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