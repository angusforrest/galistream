import argparse
import numpy
import matplotlib.pyplot as plt
import pickle
import os
import math

def split_orbits(orbits):
	print("split branch")
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
				yield gen[num*i:end]
	for i, x in enumerate(generator_split(orbits)):
		with open(f"orbit{i}.pickle","wb") as file:
			pickle.dump(x,file)

def fetch_orbit_data(input,filename):
    ts = input.t
    print("fetch branch")
    res = [input.E(t=ts),input.Lz(t=ts)]
    print(res)
    with open(f"done_{filename}","wb") as file:
        pickle.dump(res,file)
    return 0

def main():
	parser = argparse.ArgumentParser("momentum")

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
		split_orbits(data)
	else:
		fetch_orbit_data(data,args.filename)
	return 0

if __name__ == '__main__':
    main()
