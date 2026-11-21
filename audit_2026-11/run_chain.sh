#!/bin/zsh
# usage: run_chain.sh d sortedDigits nshards   -> out_<d>_<digits>.txt
d=$1; F=$2; ns=$3; rm -f shard_${d}_${F}_*.txt
for s in $(seq 0 $((ns-1))); do ./chain $d $F $s $ns > shard_${d}_${F}_$s.txt & done; wait
cat shard_${d}_${F}_*.txt > out_${d}_${F}.txt; rm -f shard_${d}_${F}_*.txt
