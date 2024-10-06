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

def diagnostic_dist(orbits):
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
	for i, x in enumerate(generator_split(orbits)):
		with open(f"temp_orbit{i}.pickle","wb") as file:
			pickle.dump(x,file)
	return 0

def plot_diagnostics(input):
	for i,orbit in input:
		print(i,orbit)
		plot_diagnostic(orbit,i)

def plot_diagnostic(orbit,i):
	plt.ioff()
	fig, ax = plt.subplots(3, 3, figsize=(25, 15), sharex=True)
	ts = orbit.t
	ax[0, 0].plot(ts, orbit.x(ts))
	ax[1, 0].plot(ts, orbit.y(ts))
	ax[2, 0].plot(ts, orbit.z(ts))
	ax[0, 1].plot(ts, orbit.vx(ts))
	ax[1, 1].plot(ts, orbit.vy(ts))
	ax[2, 1].plot(ts, orbit.vz(ts))
	ax[0, 2].plot(ts, orbit.E(ts))
	ax[1, 2].plot(ts, orbit.Lz(ts))
	ax[0, 0].set_xlabel(f"t (Gyr)")
	ax[0, 0].set_ylabel(f"x (kpc)")
	ax[1, 0].set_xlabel(f"t (Gyr)")
	ax[1, 0].set_ylabel(f"y (kpc)")
	ax[2, 0].set_xlabel(f"t (Gyr)")
	ax[2, 0].set_ylabel(f"z (kpc)")
	ax[0, 1].set_xlabel(f"t (Gyr)")
	ax[0, 1].set_ylabel(f"vx (kpc)")
	ax[1, 1].set_xlabel(f"t (Gyr)")
	ax[1, 1].set_ylabel(f"vy (kpc)")
	ax[2, 1].set_xlabel(f"t (Gyr)")
	ax[2, 1].set_ylabel(f"vz (kpc)")
	ax[0, 2].set_xlabel(f"t (Gyr)")
	ax[0, 2].set_ylabel(f"E (km^2/s^2)")
	ax[1, 2].set_xlabel(f"t (Gyr)")
	ax[1, 2].set_ylabel(f"Lz ()")
	ax[2, 2].set_xlabel(f"t (Gyr)")
	ax[2, 2].set_ylabel(f"s (km/s)")
	print("saving diagnostic view")
	plt.savefig(f"diagnostic{i:05d}.png", dpi=300)
	plt.close()

def main():
	parser = argparse.ArgumentParser("diagnostic")

	parser.add_argument("-s","--split",default=False)
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
		diagnostic_dist(data)
	else:
		plot_diagnostics(data)
	return 0

if __name__ == '__main__':
	main()
