#!/bin/bash

cd kicad-library-utils/klc-check
python3 check_symbol.py -vv ../../fab.kicad_sym
FPS=$(ls ../../fab.pretty/*.kicad_mod)
for FP in ${FPS}
do
  python3 check_footprint.py ${FP}
done
