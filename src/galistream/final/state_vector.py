import argparse
import numpy
import matplotlib.pyplot as plt
from astropy import units as u
import galpy
import pickle 
import os
import math
from multiprocessing.pool import Pool
from galpy.util import conversion

def plot_state(truth,deflect):
	plt.ioff()
	orbit0 = truth[0]
	orbit1 = deflect[0]
	fig, ax = plt.subplots(2, 3, figsize=(8, 4), sharex=True)
	ts = orbit0.t
	ts0 = numpy.linspace(0,1,len(ts))
	fig.set_tight_layout(True)
	ax[0, 0].plot(ts0, orbit0.x(ts))
	ax[0, 1].plot(ts0, orbit0.y(ts))
	ax[0, 2].plot(ts0, orbit0.z(ts))
	ax[1, 0].plot(ts0, orbit0.vx(ts))
	ax[1, 1].plot(ts0, orbit0.vy(ts))
	ax[1, 2].plot(ts0, orbit0.vz(ts))
	ax[0, 0].plot(ts0, orbit1.x(ts))
	ax[0, 1].plot(ts0, orbit1.y(ts))
	ax[0, 2].plot(ts0, orbit1.z(ts))
	ax[1, 0].plot(ts0, orbit1.vx(ts))
	ax[1, 1].plot(ts0, orbit1.vy(ts))
	ax[1, 2].plot(ts0, orbit1.vz(ts))
	for x in ax.flatten():
		x.set_xlim(0,1)
	ax[0, 0].set_ylabel(f"x (kpc)")
	ax[0, 1].set_ylabel(f"y (kpc)")
	ax[0, 2].set_ylabel(f"z (kpc)")
	ax[1, 0].set_xlabel(f"t (Gyr)")
	ax[1, 0].set_ylabel(f"vx (kpc)")
	ax[1, 1].set_xlabel(f"t (Gyr)")
	ax[1, 1].set_ylabel(f"vy (kpc)")
	ax[1, 2].set_xlabel(f"t (Gyr)")
	ax[1, 2].set_ylabel(f"vz (kpc)")
	plt.savefig(f"statevector.png", dpi=300)
	plt.close()

def main():
	parser = argparse.ArgumentParser("state vector")
	parser.add_argument("truth")
	parser.add_argument("deflect")
	args =parser.parse_args()
	if os.path.exists(args.truth):
		with open(args.truth, "rb") as file:
			truth = pickle.load(file)
	else:
		print("file provided does not exist")
		return 0
	if os.path.exists(args.deflect):
		with open(args.deflect, "rb") as file:
			deflect = pickle.load(file)
	else:
		print("file provided does not exist")
		return 0
	plot_state(truth,deflect)
	return 0

if __name__ == '__main__':
	main()
