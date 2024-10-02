import argparse
import numpy
import math
import matplotlib.pyplot as plt
import pickle
import os

def plot_dist(orbits):
	ts = numpy.array(orbits.t[numpy.arange(0,len(orbits.t),4)])
	if not ("OMP_NUM_THREADS" in os.environ):
		print("OMP_NUM_THREADS environmental variable not set")
		return 0 
	def generator_split(gen):
		cores = int(os.environ.get("OMP_NUM_THREADS"))
		if cores == 1:
			 yield gen
		else:
			num = math.ceil(gen.size / (cores))
			finish = 0
			for i in range(cores):
				if finish == 1:
					break
				end = num*(i+1)
				if end > gen.size:
					yield gen[num*i:gen.size]
					finish = 1
				yield gen[num*i:end]
	for i, x in enumerate(generator_split(ts)):
		with open(f"temp_orbit{i:03d}.pickle","wb") as file:
			pickle.dump(x,file)
	return 0

def plot_scatters(orbits,gmc,ts):
    for t in ts:
        plot_scatter(orbits,gmc,t)

def plot_scatter(orbits,gmc,t):
    plt.ioff()
    ax = plt.axes(projection='3d',computed_zorder=false)
    ax.set_xlabel(f"x (kpc)")
    ax.set_ylabel(f"y (kpc)")
    iso = numpy.array([orbits.x(t),orbits.y(t),orbits.z(t)])
    select = orbits.z(t) > 0
    ax.scatter(orbits.x(t)[select],orbits.y(t)[select],orbits.z(t)[select],s=1,zorder=1)
    ax.scatter(gmc.x(t),gmc.y(t),gmc.z(t),zorder=0,s=1)
    ax.scatter(orbits.x(t)[numpy.logical_not(select)],orbits.y(t)[numpy.logical_not(select)],orbits.z(t)[numpy.logical_not(select)],s=1,zorder=-1)
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_zlim(-1,1)
    plt.savefig(f"frame{t:013.10f}.png",dpi=300)
    plt.close()
    
def main():
	parser = argparse.ArgumentParser("3d_plot")

	parser.add_argument("-s","--split",default=False)
	parser.add_argument("-p","--process",default=False)
	parser.add_argument("-g","--gmc",default=False)
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
			with open(args.process, "rb") as file:
				ts = pickle.load(file)
		else:
			print("file provided does not exist")
			return 0
		if os.path.exists(args.gmc):
			with open(args.gmc, "rb") as file:
				gmc = pickle.load(file)
		else:
			print("file provided does not exist")
			return 0
		plot_scatters(data,gmc,ts)
	return 0

if __name__ == '__main__':
    main()
