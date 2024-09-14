import os
import argparse
import pickle

import numpy
from astropy import units as u
from galpy.potential import (MovingObjectPotential,MWPotential,PlummerPotential,)
from galpy.orbit import Orbit

def create_potentials(progress,time,lifetime,num):
    if not ("OMP_NUM_THREADS" in os.environ):
        print("OMP_NUM_THREADS environmental variable not set")
        return 0
    return 0
    ts = np.linspace(0.0,time,2001)*u.Gyr

    if lifetime != None:
        print("lifetime on gmc currently not implemented")
        return 0

    orbits = Orbit([distributionGMC(rin,rout) for x in range(num)])
    orbits.integrate(ts, MWPotential2014, method="dop853")
    
    plum = PlummerPotential(amp=1e5*u.Msun, b=200*u.pc)
    potential = [MovingObjectPotential(orbit=orbit, pot=plum) for orbit in orbits]    
    return potential

def main():
    parser = argparse.ArgumentParser("gmc_potential")
    parser.add_argument("-p","--progress",default=False)
    parser.add_argument("-t","--time",default=1.0)
    parser.add_argument("-l","--lifetime",default=None)
    parser.add_argument("-n","--num",default=5000)
    parser.add_argument("-o","--output",default=".",help="default output directory")
    args = parser.parse_args()

    if args.output != ".":
        if not os.path.isdir(args.output):
            os.makedirs(args.output)
        os.chdir(args.output)

    potential = create_potentials(args.progress,args.time,args.lifetime,args.num)

    with open("gmc_potential.pickle","wb") as file:
        pickle.dump(potential,file)    

if __name__ == '__main__':
    main()
