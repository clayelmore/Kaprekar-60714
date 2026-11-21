#!/bin/sh
# Referee batch: full multiset enumeration (enum) and all-m superset check (allm).
cd "$(dirname "$0")"
{
for b in $(seq 3 60); do echo "3 $b enum"; done
for b in $(seq 3 32); do echo "4 $b enum"; done
for b in $(seq 3 22); do echo "5 $b enum"; done
for b in $(seq 3 18); do echo "6 $b enum"; done
for b in $(seq 3 14); do echo "7 $b enum"; done
for b in $(seq 3 11); do echo "8 $b enum"; done
for b in 100 150 200 255 300 333 400; do echo "3 $b allm"; done
for b in 40 50 64 75 90; do echo "4 $b allm"; done
for b in 25 30 37 40; do echo "5 $b allm"; done
for b in 19 20 21; do echo "6 $b allm"; done
} | xargs -P 16 -L 1 ./ref_hs > results_raw.txt 2>&1
sort -t= -k2,2n -k3,3n results_raw.txt > results.txt
