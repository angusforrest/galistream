import argparse
import numpy
import math
import matplotlib.pyplot as plt
import pickle
import os

def slice_plot_scatter(orbits,gmc):
	ts = numpy.array(orbits.t[numpy.arange(0,len(orbits.t),4)])
	COL3 = '#FFBA08'
	COL2 = '#F48C06'
	COL1 = '#DC2F02'
	COL0 = '#9D0208'
	COLWHITE = '#F7F7F8'
	COLBLACK = '#001134'
	plt.ioff()
	fig,ax = plt.subplots(4,3,figsize=(20,15))
	t = ts[0]
	ax[0,0].scatter(orbits.x(t),orbits.z(t),s=1,color=COL3)
	ax[0,0].scatter(gmc.x(t),gmc.z(t),s=1,color=COL1)
	ax[0,0].set_xlim(-9,9)
	ax[0,0].set_ylim(-1,1)
	ax[0,0].set_xlabel("x (kpc)")
	ax[0,0].set_ylabel("z (kpc)")
	ax[0,1].scatter(orbits.y(t),orbits.z(t),s=1,color=COL3)
	ax[0,1].scatter(gmc.y(t),gmc.z(t),s=1,color=COL1)
	ax[0,1].set_xlim(-9,9)
	ax[0,1].set_ylim(-1,1)
	ax[0,1].set_xlabel("y (kpc)")
	ax[0,1].set_ylabel("z (kpc)")
	ax[0,1].scatter(orbits.x(t),orbits.y(t),s=1,color=COL3)
	ax[0,1].set_xlim(-9,9)
	ax[0,1].set_ylim(-9,9)
	ax[0,1].set_xlabel("x (kpc)")
	ax[0,1].set_ylabel("y (kpc)")
	t = ts[150]
	ax[1,0].scatter(orbits.x(t),orbits.z(t),s=1,color=COL3)
	ax[1,0].scatter(gmc.x(t),gmc.z(t),s=1,color=COL1)
	ax[1,0].set_xlim(-9,9)
	ax[1,0].set_ylim(-1,1)
	ax[1,0].set_xlabel("x (kpc)")
	ax[1,0].set_ylabel("z (kpc)")
	ax[1,1].scatter(orbits.y(t),orbits.z(t),s=1,color=COL3)
	ax[1,1].scatter(gmc.y(t),gmc.z(t),s=1,color=COL1)
	ax[1,1].set_xlim(-9,9)
	ax[1,1].set_ylim(-1,1)
	ax[1,1].set_xlabel("y (kpc)")
	ax[1,1].set_ylabel("z (kpc)")
	ax[1,1].scatter(orbits.x(t),orbits.y(t),s=1,color=COL3)
	ax[1,1].set_xlim(-9,9)
	ax[1,1].set_ylim(-9,9)
	ax[1,1].set_xlabel("x (kpc)")
	ax[1,1].set_ylabel("y (kpc)")
	t = ts[300]
	ax[2,0].scatter(orbits.x(t),orbits.z(t),s=1,color=COL3)
	ax[2,0].scatter(gmc.x(t),gmc.z(t),s=1,color=COL1)
	ax[2,0].set_xlim(-9,9)
	ax[2,0].set_ylim(-1,1)
	ax[2,0].set_xlabel("x (kpc)")
	ax[2,0].set_ylabel("z (kpc)")
	ax[2,1].scatter(orbits.y(t),orbits.z(t),s=1,color=COL3)
	ax[2,1].scatter(gmc.y(t),gmc.z(t),s=1,color=COL1)
	ax[2,1].set_xlim(-9,9)
	ax[2,1].set_ylim(-1,1)
	ax[2,1].set_xlabel("y (kpc)")
	ax[2,1].set_ylabel("z (kpc)")
	ax[2,1].scatter(orbits.x(t),orbits.y(t),s=1,color=COL3)
	ax[2,1].set_xlim(-9,9)
	ax[2,1].set_ylim(-9,9)
	ax[2,1].set_xlabel("x (kpc)")
	ax[2,1].set_ylabel("y (kpc)")
	t = ts[-1]
	ax[3,0].scatter(orbits.x(t),orbits.z(t),s=1,color=COL3)
	ax[3,0].scatter(gmc.x(t),gmc.z(t),s=1,color=COL1)
	ax[3,0].set_xlim(-9,9)
	ax[3,0].set_ylim(-1,1)
	ax[3,0].set_xlabel("x (kpc)")
	ax[3,0].set_ylabel("z (kpc)")
	ax[3,1].scatter(orbits.y(t),orbits.z(t),s=1,color=COL3)
	ax[3,1].scatter(gmc.y(t),gmc.z(t),s=1,color=COL1)
	ax[3,1].set_xlim(-9,9)
	ax[3,1].set_ylim(-1,1)
	ax[3,1].set_xlabel("y (kpc)")
	ax[3,1].set_ylabel("z (kpc)")
	ax[3,2].scatter(orbits.x(t),orbits.y(t),s=1,color=COL3)
	ax[3,2].set_xlim(-9,9)
	ax[3,2].set_ylim(-9,9)
	ax[3,2].set_xlabel("x (kpc)")
	ax[3,2].set_ylabel("y (kpc)")
	plt.savefig(f"spatial_map.png",dpi=300)
	plt.savefig(f"spatial_map.svg",dpi=300)
	plt.close()

def plot_scatter(orbits,gmc):
	ts = numpy.array(orbits.t[numpy.arange(0,len(orbits.t),4)])
	COL3 = '#FFBA08'
	COL2 = '#F48C06'
	COL1 = '#DC2F02'
	COL0 = '#9D0208'
	COLWHITE = '#F7F7F8'
	COLBLACK = '#001134'
	plt.ioff()
	fig = plt.figure()
	ax = fig.add_subplot(2, 2, 1, projection='3d',computed_zorder=False)
	ax.grid(False)
	#ax.set_xticks([])
	#ax.set_yticks([])
	#ax.set_zticks([])
	#ax.set_axis_off()
	t = ts[0]
	iso = numpy.array([orbits.x(t),orbits.y(t),orbits.z(t)])
	select = orbits.z(t) > 0
	ax.scatter(orbits.x(t)[select],orbits.y(t)[select],orbits.z(t)[select],s=1,zorder=1,color=COL3,depthshade=False)
	ax.scatter(gmc.x(t),gmc.y(t),gmc.z(t),zorder=0,s=1,color=COL1,depthshade=False,alpha=0.2)
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
	ax = fig.add_subplot(2, 2, 2, projection='3d',computed_zorder=False)
	ax.grid(False)
	#ax.set_xticks([])
	#ax.set_yticks([])
	#ax.set_zticks([])
	#ax.set_axis_off()
	t = ts[20]
	iso = numpy.array([orbits.x(t),orbits.y(t),orbits.z(t)])
	select = orbits.z(t) > 0
	ax.scatter(orbits.x(t)[select],orbits.y(t)[select],orbits.z(t)[select],s=1,zorder=1,color=COL3,depthshade=False)
	ax.scatter(gmc.x(t),gmc.y(t),gmc.z(t),zorder=0,s=1,color=COL1,depthshade=False,alpha=0.2)
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
	ax = fig.add_subplot(2, 2, 3, projection='3d',computed_zorder=False)
	ax.grid(False)
	#ax.set_xticks([])
	#ax.set_yticks([])
	#ax.set_zticks([])
	#ax.set_axis_off()
	t = ts[35]
	iso = numpy.array([orbits.x(t),orbits.y(t),orbits.z(t)])
	select = orbits.z(t) > 0
	ax.scatter(orbits.x(t)[select],orbits.y(t)[select],orbits.z(t)[select],s=1,zorder=1,color=COL3,depthshade=False)
	ax.scatter(gmc.x(t),gmc.y(t),gmc.z(t),zorder=0,s=1,color=COL1,depthshade=False,alpha=0.2)
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
	ax = fig.add_subplot(2, 2, 4, projection='3d',computed_zorder=False)
	ax.grid(False)
	#ax.set_xticks([])
	#ax.set_yticks([])
	#ax.set_zticks([])
	#ax.set_axis_off()
	t = ts[-1]
	iso = numpy.array([orbits.x(t),orbits.y(t),orbits.z(t)])
	select = orbits.z(t) > 0
	ax.scatter(orbits.x(t)[select],orbits.y(t)[select],orbits.z(t)[select],s=1,zorder=1,color=COL3,depthshade=False)
	ax.scatter(gmc.x(t),gmc.y(t),gmc.z(t),zorder=0,s=1,color=COL1,depthshade=False,alpha=0.2)
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
	slice_plot_scatter(data,gmc)
	return 0

if __name__ == '__main__':
    main()
