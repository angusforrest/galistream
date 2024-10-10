import argparse
import numpy
import math
import matplotlib.pyplot as plt
import pickle
import os

def plot_scatter(orbits,gmc):
    COL3 = '#1E9CBF'
    COL2 = '#1EBF74'
    COL1 = '#BEA61E'
    COL0 = '#BE681E'
    COLWHITE = '#F7F7F8'
    COLBLACK = '#001134'
    plt.ioff()
    ax = plt.axes(projection='3d',computed_zorder=False,figsize=(12.56,29.7))
    ax.grid(False)
    offset = 0
    ts = np.array([300,320,340,360])-offset
    for t in ts:
	    ax.set_xticks([])
		ax.set_yticks([])
		ax.set_zticks([])
	    ax.set_xlabel(f"x (kpc)")
	    ax.set_ylabel(f"y (kpc)")
	    iso = numpy.array([orbits.x(t),orbits.y(t),orbits.z(t)])
	    select = orbits.z(t) > 0
	    ax.scatter(orbits.x(t)[select],orbits.y(t)[select],orbits.z(t)[select],s=1,zorder=1,color='#aaa')
	    ax.scatter(gmc.x(t),gmc.y(t),gmc.z(t),zorder=0,s=1,color='#fff')
	    ax.scatter(orbits.x(t)[numpy.logical_not(select)],orbits.y(t)[numpy.logical_not(select)],orbits.z(t)[numpy.logical_not(select)],s=1,zorder=-1,color='#aaa')
	    ax.set_xlim(-10,10)
	    ax.set_ylim(-10,10)
	    ax.set_zlim(-1,1)
    plt.savefig("spatial_map.png",dpi=600,transparent=True)
    plt.savefig("spatial_map.svg",dpi=600,transparent=True)
    plt.close()
    
def main():
	parser = argparse.ArgumentParser("3d_plot")
	parser.add_argument("-g","--gmc",default=False)
	parser.add_argument("filename")
	args =parser.parse_args()
	if os.path.exists(args.filename):
		with open(args.filename, "rb") as file:
			data = pickle.load(file)
	else:
		print("file provided does not exist")
		return 0
	if os.path.exists(args.gmc):
		with open(args.gmc, "rb") as file:
			gmc = pickle.load(file)
	else:
		print("file provided does not exist")
		return 0
	plot_scatter(data,gmc)
	return 0

if __name__ == '__main__':
    main()
