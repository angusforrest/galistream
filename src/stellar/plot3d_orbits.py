import argparse
import numpy
import math
import matplotlib.pyplot as plt
import pickle
import os
from multiprocessing.pool import Pool
from functools import partial

def animate_orbits(orbits):
	if not ("OMP_NUM_THREADS" in os.environ):
		print("OMP_NUM_THREADS environmental variable not set")
		return 0 
	def generator_split(gen):
		cores = int(os.environ.get("OMP_NUM_THREADS"))
		if cores == 1:
			 yield gen
		else:
			num = math.ceil(gen.size / (cores))
			for i in range(cores):
				end = num*(i+1)
				if i == cores - 1:
					end = gen.size
				yield zip(numpy.arange(num*i,end,1),gen[num*i:end])
	for i, x in enumerate(generator_split(np.arange(0,orbits.t,4)):
		with open(f"temp_orbit{i}.pickle","wb") as file:
			pickle.dump(x,file)
	return 0

def plot_scatters(orbits,ts):
    for t in ts:
        plot_orbit(orbits,t)

def plot_scatter(orbits,t):
    pyplot.ioff()
    ax = plt.axes()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_zlim(-2,2)
    ax.set_xlabel(f"x (kpc)")
    ax.set_ylabel(f"y (kpc)")
    ax.scatter3d(orbits.x(t),orbits.y(t),orbits.z(t),s=1)
    plt.savefig(f"frame{t}.png",dpi=300)
    plt.close()
    
def main():
	parser = argparse.ArgumentParser("3d_plot")

	parser.add_argument("-s","--split",default=False)
	parser.add_argument("-p","--process",default=False)
	parser.add_argument("filename")
	args =parser.parse_args()
	if os.path.exists(args.filename):
		with open(args.filename, "rb") as file:
			data = pickle.load(file)
	else:
		print("file provided does not exist")
		return 0
	if bool(args.split) == True:
		print("split")
		plot_dist(data)
	else:
    	if os.path.exists(args.process):
    		with open(args.filename, "rb") as file:
    			ts = pickle.load(file)
    	else:
    		print("file provided does not exist")
    		return 0
		plot_scatters(data,ts)
	return 0

if __name__ == '__main__':
    main()
