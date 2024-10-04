#!/bin/bash
find . -type f -name 'temp*' -print0 | xargs -I {} -0 -P 47 python ~/stellar/src/stellar/plot3d_orbits.py -g gmc_orbits.pickle -p {} deflect.pickle
