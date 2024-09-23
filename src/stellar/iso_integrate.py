import pickle
import argparse
import numpy
import os
from galpy.potential import MWPotential2014
from galpy.orbit import Orbit
from astropy import units as u

def coordinate(x,y,z,vx,vy,vz):
    r = numpy.sqrt(x*x + y*y)
    vR = (x * vx + y * vy) /r
    vT = (x* vy - y *vx) /r
    phi = numpy.arctan2(y,x)
    pcMyr = u.pc / u.Myr
    return [
        r * u.pc,
        vR *pcMyr,
        vT *pcMyr,
        z * u.pc,
        vz *pcMyr,
        phi*u.rad,
    ]


    
def import_iso(fname):
    data = [coordinate(*x) for x in numpy.loadtxt(fname)]
    return Orbit(data)


def integrate(orbits,pot):
    ts = pot[0]._orb.t
    truth = orbits[:]
    deflect = orbits[:]
    truth.integrate(ts,pot=MWPotential2014, method="dop853_c")
    for i in range(math.ceil(len(deflect)/200)):
        end = 200*(i+1)
        if end > len(deflect):
            end = len(deflect)
        deflect[200*i,end].integrate(ts,pot=MWPotential2014 + pot, method="dop853_c")
        with open(f"temp_orbits_{i}.pickle","wb") as file:
            pickle.dump(deflect,file)
    return truth, deflect

def main():
    parser = argparse.ArgumentParser("iso_integrate")
    parser.add_argument("gmc_file")
    parser.add_argument("iso_file")
    args = parser.parse_args()
    if not os.path.exists(args.gmc_file):
        print("gmc_file does not exist")
        return 0
    if not os.path.exists(args.iso_file):
        print("iso_file does not exist")
        return 0
    iso_orbits = import_iso(args.iso_file)
    with open(args.gmc_file,"rb") as file:
        gmc_potentials = pickle.load(file)
    truth, deflect = integrate(iso_orbits,gmc_potentials)
    with open("truth.pickle","wb") as file:
        pickle.dump(truth,file)
    with open("deflect.pickle","wb") as file:
        pickle.dump(deflect,file)
    return 0

if __name__ == '__main__':
    main()
