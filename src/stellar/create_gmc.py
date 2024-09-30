import os
import argparse
import pickle

import numpy
from astropy import units as u
from galpy.potential import (MovingObjectPotential,MWPotential2014,PlummerPotential,vcirc,)
from galpy.orbit import Orbit
from galpy.util import conversion

def distributionGMC(rin, rout):
    phi = numpy.random.rand()
    r = numpy.sqrt(numpy.random.rand() * (rout * rout - rin * rin) + rin * rin)
    vc = vcirc(MWPotential2014, r)
    kms = u.km/u.s
    return [
        r,
        0.0*kms,
        vc * 220.0 *kms,
        0.0*u.kpc,
        0.0*kms,
        phi* 360.0*u.deg
    ]
def create_orbits(progress,ts,num,rin,rout):
    orbits = Orbit([distributionGMC(rin,rout) for x in range(num)])
    orbits.integrate(ts, MWPotential2014, method="dop853_c",progressbar=progress)
    return orbits
    
def create_potentials(progress,time,lifetime,num,rin,rout):
    if not ("OMP_NUM_THREADS" in os.environ):
        print("OMP_NUM_THREADS environmental variable not set")
        return 0
    ts = conversion.parse_time(numpy.linspace(0.0,time,2001)*u.Gyr,ro=8.0,vo=220.0)

    if lifetime != None:
        print("lifetime on gmc currently not implemented")
        return 0
    orbits = create_orbits(progress,ts,num,rin,rout)
    plum = PlummerPotential(amp=1e5*u.Msun, b=200*u.pc)
    potential = [MovingObjectPotential(orbit=orbit, pot=plum) for orbit in orbits]    
    return orbits, potential

def main():
    parser = argparse.ArgumentParser("gmc_potential")
    parser.add_argument("-p","--progress",default=False,type=bool)
    parser.add_argument("-t","--time",default=1.0)
    parser.add_argument("-l","--lifetime",default=None)
    parser.add_argument("-n","--num",default=5000)
    parser.add_argument("-o","--output",default=".",help="default output directory")
    parser.add_argument("-rin","--rin",default=7.0*u.kpc)
    parser.add_argument("-rout","--rout",default=9.0*u.kpc)
    args = parser.parse_args()
    if args.output != ".":
        if not os.path.isdir(args.output):
            os.makedirs(args.output)
        os.chdir(args.output)

    orbits, potential = create_potentials(args.progress,float(args.time),float(args.lifetime),int(args.num),float(args.rin),float(args.rout))
    with open("gmc_orbits.pickle","wb") as file:
        pickle.dump(orbits,file)
    with open("gmc_potential.pickle","wb") as file:
        pickle.dump(potential,file)    

if __name__ == '__main__':
    main()
