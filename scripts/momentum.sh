#!/bin/bash
find . -type f -name 'orbit*' -print0 | xargs -I {} -0 -P 53 python ~/stellar/src/stellar/momentum.py {}
