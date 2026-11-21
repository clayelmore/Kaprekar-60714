#!/usr/bin/env python3
"""Audit 2026-11: complete enumeration at d=28 of the m=7 'clean repeat' witness rule
(multiplicity_chain/m7_witness.json), previously supported only by sampling."""
import json, subprocess
w = json.load(open('../multiplicity_chain/m7_witness.json')); perms = w['block_place_value_perms']
A=[3,2,1,0]; B=[0,1,2,3]; c=[0]*28
for i in range(4):
    for s in range(7):
        sh=4*perms[i][s]; c[7*i+s]=10**(A[i]+sh)-10**(B[i]+sh)
print(subprocess.run(['./kap','28']+[str(x) for x in c],capture_output=True,text=True).stdout)
