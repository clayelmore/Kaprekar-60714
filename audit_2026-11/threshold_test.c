// Threshold test for extended N-letter cores (2026-11-27).  Build: cc -O2 -DN=7 -o threshold_test7 threshold_test.c
// Same rule family and same map Phi as closure_all.c, but instead of stopping silently at the first
// failure it reports WHY a core fails the all-lengths closure check and how many nonzero digits the
// failing orbit ever holds (pathmax). A failing orbit whose states all have at most W nonzero digits is a
// real orbit of the extended rule at every length d > W (each state then has a zero digit, so Phi is the
// rule). So a core with a failing witness of pathmax = W is NOT universal at any length d > W.
// Classes printed, one line per core:
//   L0     K = 0 on some non-repdigit with the six-digit shape (fails at every length)
//   T:<r>  the orbit of {1} does not end in a fixed point (r = zero | cycle | long | overflow), with pathmax
//   S:<r>  (pathmax here is the larger of the failing seed's orbit and the orbit of {1} up to the target)
//          some seed (#9 <= N-1, #non9 <= 9+N) does not reach the target (r = zero | cycle | overflow | lowrange |
//          tablefull), with pathmax of that seed's orbit
//   PASS   closure holds (KNOWN = listed in the optional file of cores already known to pass; not rerun)
// usage: threshold_test shard nshards [file with one 'a b' digit-string pair per line]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#ifndef N
#define N 6
#endif
typedef uint64_t u64; typedef int64_t i64;
#define HB 24
static u64 *keys; static int16_t *val; static uint32_t *stamp; static uint32_t gen=1;
static u64 mask=((u64)1<<HB)-1; static u64 nkeys=0;
static i64 C[N],PX,PY,P10N;
static int lowbad=0;
static inline u64 pack(const int*c){ u64 k=0; for(int g=1;g<=9;g++) k=(k<<7)|(u64)c[g]; return k+1; }
static inline u64 slot(u64 k){ u64 h=(k*0x9E3779B97F4A7C15ULL)>>(64-HB); while(stamp[h]==gen&&keys[h]!=k) h=(h+1)&mask; return h; }
static int size(const int*c){ int s=0; for(int g=1;g<=9;g++) s+=c[g]; return s; }
static void phi(const int*c,int*o){ int n[1300]; int k=0; for(int g=9;g>=1;g--) for(int i=0;i<c[g];i++) n[k++]=g; for(int i=k;i<k+N+2;i++) n[i]=0;
  i64 L=-PY*n[N-1]; for(int i=0;i<N-1;i++) L+=C[i]*n[i];
  static int dig[1310]; memset(dig,0,sizeof dig); int top=0; for(int j=N;j<=k;j++){ dig[j]=n[j-1]-n[j]; if(dig[j]) top=j; }
  memset(o,0,10*sizeof(int));
  if(top==0){ i64 v=L<0?-L:L; while(v){ o[v%10]++; v/=10; } o[0]=0; return; }
  i64 low; if(L>=0) low=L; else { low=P10N+L; int j=N; while(dig[j]==0){ dig[j]=9; j++; } dig[j]--; }
  if(low<0||low>=P10N){ lowbad=1; return; }
  for(int j=0;j<N;j++){ dig[j]=low%10; low/=10; }
  for(int j=0;j<=top;j++) o[dig[j]]++; o[0]=0; }
static const char*why; static int pathmax; static int failed; static int tmax;
static u64 nseeds; static int maxsteps, maxsize;
static void run(const int*c0){ static u64 path[100000]; int np=0; int c[10]; memcpy(c,c0,sizeof c); int base; int pm=0;
  while(1){ for(int g=1;g<=9;g++) if(c[g]>127){ why="overflow"; pathmax=pm; failed=1; return; }
    int s=size(c); if(s>pm) pm=s;
    if(s==0){ why="zero"; pathmax=pm; failed=1; return; }
    u64 k=pack(c); u64 h=slot(k);
    if(stamp[h]==gen){ if(val[h]==-2){ why="cycle"; pathmax=pm; failed=1; return; } base=val[h]; break; }
    keys[h]=k; stamp[h]=gen; val[h]=-2; nkeys++; if(nkeys>(mask>>1)*1.6){ why="tablefull"; pathmax=pm; failed=1; return; } path[np++]=h;
    if(np>=100000){ why="long"; pathmax=pm; failed=1; return; }
    int o[10]; lowbad=0; phi(c,o); if(lowbad){ why="lowrange"; pathmax=pm; failed=1; return; } memcpy(c,o,sizeof c); }
  if(pm>maxsize) maxsize=pm;
  for(int i=np-1;i>=0;i--){ base++; val[path[i]]=base; } if(base>maxsteps) maxsteps=base; nseeds++; }
static void rec(int g,int left,int*c){ if(failed) return; if(g==0){ for(int t=0;t<=N-1&&!failed;t++){ c[9]=t; if(size(c)) run(c); } c[9]=0; return; } for(int k=0;k<=left&&!failed;k++){ c[g]=k; rec(g-1,left-k,c); } c[g]=0; }
// returns 0 L0, 1 T fail, 2 S fail, 3 pass
static int l0bad; static int T0[N];
static void lem0(int i,int hi){ if(l0bad) return; if(i==N){ if(T0[0]==T0[N-1]) return; i64 v=(PX-PY)*T0[N-1]; for(int k=0;k<N-1;k++) v+=C[k]*T0[k]; if(v==0) l0bad=1; return; }
  for(int t=hi;t>=0;t--){ T0[i]=t; lem0(i+1,t); } }
static int check(const int*a,const int*b,int*f){ for(int i=0;i<N-1;i++){ i64 pa=1,pb=1; for(int k=0;k<a[i];k++)pa*=10; for(int k=0;k<b[i];k++)pb*=10; C[i]=pa-pb; } PX=1;PY=1; for(int i=0;i<a[N-1];i++)PX*=10; for(int i=0;i<b[N-1];i++)PY*=10; P10N=1; for(int i=0;i<N;i++)P10N*=10;
  l0bad=0; lem0(0,9); if(l0bad) return 0;
  gen++; nkeys=0; nseeds=0; maxsteps=0; maxsize=0; failed=0; pathmax=0;
  int c[10]={0},o[10]; c[1]=1; static u64 seen[4000]; int ns=0; int pm=0;
  while(1){ int s=size(c); if(s>pm) pm=s; pathmax=pm;
    if(s==0){ why="zero"; return 1; }
    for(int g=1;g<=9;g++) if(c[g]>127){ why="overflow"; return 1; }
    u64 k=pack(c); for(int i=0;i<ns;i++) if(seen[i]==k){ why="cycle"; return 1; }
    lowbad=0; phi(c,o); if(lowbad){ why="lowrange"; return 1; }
    if(!memcmp(o+1,c+1,9*sizeof(int))) break; if(ns>=4000){ why="long"; return 1; } seen[ns++]=k; memcpy(c,o,sizeof c); }
  tmax=pm; memcpy(f,c,10*sizeof(int)); f[0]=0; u64 h=slot(pack(f)); keys[h]=pack(f); stamp[h]=gen; val[h]=0; nkeys++; int cc[10]={0}; rec(8,9+N,cc);
  return failed?2:3; }
static int A[N],B[N],UA[N],UB[N]; static long idx=0; static int SH,NS;
static u64 *known; static long nknown=0;
static int cmpu(const void*x,const void*y){ u64 a=*(const u64*)x,b=*(const u64*)y; return a<b?-1:a>b; }
static u64 keyab(void){ u64 k=0; for(int i=0;i<N;i++) k=k*10+A[i]; for(int i=0;i<N;i++) k=k*10+B[i]; return k; }
static void gb(int i){ if(i==N){ if(idx++%NS!=SH) return; int f[10]; int r; u64 kk=keyab(); if(nknown&&bsearch(&kk,known,nknown,8,cmpu)){ printf("KNOWN a="); for(int k=0;k<N;k++)printf("%d",A[k]); printf(" b="); for(int k=0;k<N;k++)printf("%d",B[k]); printf("\n"); return; } r=check(A,B,f);
    printf("%s",r==0?"L0":r==1?"T":r==2?"S":"PASS"); if(r==2&&tmax>pathmax) pathmax=tmax; if(r==1||r==2) printf(":%s pathmax=%d",why,pathmax); if(r==3) printf(" maxsize=%d",maxsize);
    printf(" a="); for(int k=0;k<N;k++)printf("%d",A[k]); printf(" b="); for(int k=0;k<N;k++)printf("%d",B[k]); printf("\n"); return; }
  for(int p=0;p<N;p++){ if(UB[p]||p==A[i]) continue; UB[p]=1; B[i]=p; gb(i+1); UB[p]=0; } }
static void ga(int i){ if(i==N){ gb(0); return; } for(int p=0;p<N;p++){ if(UA[p]) continue; UA[p]=1; A[i]=p; ga(i+1); UA[p]=0; } }
int main(int argc,char**argv){ if(argc<3) return 1; SH=atoi(argv[1]); NS=atoi(argv[2]);
  if(argc>3){ FILE*fp=fopen(argv[3],"r"); if(!fp) return 2; known=malloc(8*100000); char sa[32],sb[32]; while(fscanf(fp,"%31s %31s",sa,sb)==2&&nknown<100000){ u64 k=0; for(char*q=sa;*q;q++) k=k*10+(*q-'0'); for(char*q=sb;*q;q++) k=k*10+(*q-'0'); known[nknown++]=k; } fclose(fp); qsort(known,nknown,8,cmpu); }
  keys=calloc(mask+1,8); val=calloc(mask+1,2); stamp=calloc(mask+1,4); ga(0); fflush(stdout); return 0; }
