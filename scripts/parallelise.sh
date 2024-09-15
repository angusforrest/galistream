#!/bin/bash
find . -type f -name 'temp*' -print0 | xargs -I {} -0 -P 8 python ../src/stellar/diagnostic.py {}
