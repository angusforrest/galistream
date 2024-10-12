import argparse
import numpy
import math
import matplotlib.pyplot as plt
import pickle
import os

def plot_scatter(orbits,gmc):
	ts = numpy.array(orbits.t[numpy.arange(0,len(orbits.t),4)])
	COL3 = '#FFBA08'
	COL2 = '#F48C06'
	COL1 = '#DC2F02'
	COL0 = '#9D0208'
	COLWHITE = '#F7F7F8'
	COLBLACK = '#001134'
	plt.ioff()
	fig = plt.figure(figsize=plt.figaspect(3))
	ax = fig.add_subplot(3, 1, 1, projection='3d',computed_zorder=False)
	ax.grid(False)
	#ax.set_xticks([])
	#ax.set_yticks([])
	#ax.set_zticks([])
	#ax.set_axis_off()
	t = ts[10]
	iso = numpy.array([orbits.x(t),orbits.y(t),orbits.z(t)])
	select = orbits.z(t) > 0
	ax.scatter(orbits.x(t)[select],orbits.y(t)[select],orbits.z(t)[select],s=1,zorder=1,color=COL3,depthshade=False)
	#ax.scatter(gmc.x(t),gmc.y(t),gmc.z(t),zorder=0,s=1,color=COL1,depthshade=False,alpha=0.5)
	ax.scatter(orbits.x(t)[numpy.logical_not(select)],orbits.y(t)[numpy.logical_not(select)],orbits.z(t)[numpy.logical_not(select)],depthshade=False,s=1,zorder=-1,color=COL3)
	ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.set_xlim(-9,9)
	ax.set_ylim(-9,9)
	ax.set_zlim(-1,1)
	ax.set_xlabel("x (kpc)")
	ax.set_ylabel("y (kpc)")
	ax.set_zlabel("z (kpc)")
	ax = fig.add_subplot(3, 1, 2, projection='3d',computed_zorder=False)
	ax.grid(False)
	#ax.set_xticks([])
	#ax.set_yticks([])
	#ax.set_zticks([])
	#ax.set_axis_off()
	t = ts[30]
	iso = numpy.array([orbits.x(t),orbits.y(t),orbits.z(t)])
	select = orbits.z(t) > 0
	ax.scatter(orbits.x(t)[select],orbits.y(t)[select],orbits.z(t)[select],s=1,zorder=1,color=COL3,depthshade=False)
	ax.scatter(gmc.x(t),gmc.y(t),gmc.z(t),zorder=0,s=1,color=COL1,depthshade=False,alpha=0.5)
	ax.scatter(orbits.x(t)[numpy.logical_not(select)],orbits.y(t)[numpy.logical_not(select)],orbits.z(t)[numpy.logical_not(select)],depthshade=False,s=1,zorder=-1,color=COL3)
	ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.set_xlim(-9,9)
	ax.set_ylim(-9,9)
	ax.set_zlim(-1,1)
	ax.set_xlabel("x (kpc)")
	ax.set_ylabel("y (kpc)")
	ax.set_zlabel("z (kpc)")
	ax = fig.add_subplot(3, 1, 3, projection='3d',computed_zorder=False)
	ax.grid(False)
	#ax.set_xticks([])
	#ax.set_yticks([])
	#ax.set_zticks([])
	#ax.set_axis_off()
	t = ts[-1]
	iso = numpy.array([orbits.x(t),orbits.y(t),orbits.z(t)])
	select = orbits.z(t) > 0
	ax.scatter(orbits.x(t)[select],orbits.y(t)[select],orbits.z(t)[select],s=1,zorder=1,color=COL3,depthshade=False)
	ax.scatter(gmc.x(t),gmc.y(t),gmc.z(t),zorder=0,s=1,color=COL1,depthshade=False,alpha=0.5)
	ax.scatter(orbits.x(t)[numpy.logical_not(select)],orbits.y(t)[numpy.logical_not(select)],orbits.z(t)[numpy.logical_not(select)],depthshade=False,s=1,zorder=-1,color=COL3)
	ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
	ax.set_xlim(-9,9)
	ax.set_ylim(-9,9)
	ax.set_zlim(-1,1)
	ax.set_xlabel("x (kpc)")
	ax.set_ylabel("y (kpc)")
	ax.set_zlabel("z (kpc)")
	plt.savefig(f"spatial_map.png",dpi=300)
	plt.savefig(f"spatial_map.svg",dpi=300)
	plt.close()

def main():
	parser = argparse.ArgumentParser("spatial_map")
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
