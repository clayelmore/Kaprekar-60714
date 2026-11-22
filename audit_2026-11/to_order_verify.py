#!/usr/bin/env python3
"""Complete enumeration of candidates printed by to_order.py.  usage: to_order_verify.py file [how_many]"""
import sys
from multiprocessing import Pool
from usage_score import score
def chk(x):
    a,b,hi,lo=x; return x,score([10**i-10**j for i,j in zip(a,b)],10)
if __name__=='__main__':
    c=[]
    for l in open(sys.argv[1]):
        if l.startswith('CAND'):
            p=l.split(); c.append((list(map(int,p[1][2:].split(','))),list(map(int,p[2][2:].split(','))),p[3],p[4]))
    mov=[x for x in c if all(i!=j for i,j in zip(x[0],x[1]))]
    pick=(mov+[x for x in c if x not in mov])[:int(sys.argv[2]) if len(sys.argv)>2 else 6]
    print(len(c),'candidates listed;',len(mov),'move every letter'); sys.stdout.flush()
    with Pool(6) as p: res=p.map(chk,pick)
    for (a,b,hi,lo),r in res:
        L=len(a); w1=[None]*L; w2=[None]*L
        for i in range(L): w1[a[i]]=i; w2[b[i]]=i
        AB='ABCDEFGHIJKLMNOPQRST'; ws=''.join(AB[w1[p]] for p in range(L-1,-1,-1))+' - '+''.join(AB[w2[p]] for p in range(L-1,-1,-1))
        print(ws,'| every letter moves' if all(i!=j for i,j in zip(a,b)) else '| has a fixed letter','|',('UNIVERSAL endpoint %d, max steps %d, mean %.1f, gaps %d/%d'%(r['F'],r['max'],r['mean'],r['gaps'],L-1)) if r else 'fails complete enumeration')
