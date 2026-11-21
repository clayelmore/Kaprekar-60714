// FIVE-letter version of closure_all.c (2026-11-21): K(s)=|sum_{k=5}^{d-1}10^k(s_{k-1}-s_k) + c0s0+..+c3s3 - 10^y s4 + 10^x s_{d-1}|, x=a_4,y=b_4.
// Extended rule at length d:  K(s) = | sum_{k=6}^{d-1} 10^k (s_{k-1}-s_k)  +  L |,
//   L = c0 s0 + c1 s1 + c2 s2 + c3 s3 + c4 s4 - 10^y s5 + 10^x s_{d-1}      (c_i = 10^a_i - 10^b_i, x=a_5, y=b_5)
// Phi = the same map on nonzero-digit multisets (valid whenever the state has a zero digit).
// Checks: (0) K=0 only on repdigits; (1) every seed (#9<=5, #non9<=15) reaches the target under Phi.
// usage: closure_gen c0 c1 c2 c3 c4 x y targetNonzeroDigits      prints one line; stops at first failure
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <setjmp.h>
static jmp_buf JB; static uint32_t *stamp; static uint32_t gen=1;
typedef uint64_t u64; typedef int64_t i64;
#define HB 23
static u64 *keys; static int16_t *val; static u64 mask=((u64)1<<HB)-1; static u64 nkeys=0;
static i64 C[4],PX,PY;
static inline u64 pack(const int*c){ u64 k=0; for(int g=1;g<=9;g++) k=(k<<7)|(u64)c[g]; return k+1; }
static inline u64 slot(u64 k){ u64 h=(k*0x9E3779B97F4A7C15ULL)>>(64-HB); while(stamp[h]==gen&&keys[h]!=k) h=(h+1)&mask; return h; }
static int maxsize=0;
static void phi(const int*c,int*o){ int n[256]; int k=0; for(int g=9;g>=1;g--) for(int i=0;i<c[g];i++) n[k++]=g; for(int i=k;i<k+8;i++) n[i]=0;
  i64 L=C[0]*n[0]+C[1]*n[1]+C[2]*n[2]+C[3]*n[3]-PY*n[4];
  int dig[260]; memset(dig,0,sizeof dig); int top=0; for(int j=5;j<=k;j++){ dig[j]=n[j-1]-n[j]; if(dig[j]) top=j; }
  memset(o,0,10*sizeof(int));
  if(top==0){ i64 v=L<0?-L:L; while(v){ o[v%10]++; v/=10; } o[0]=0; return; }
  i64 low; if(L>=0) low=L; else { low=100000+L; int j=5; while(dig[j]==0){ dig[j]=9; j++; } dig[j]--; }
  if(low<0||low>=100000){ longjmp(JB,1); }
  for(int j=0;j<5;j++){ dig[j]=low%10; low/=10; }
  for(int j=0;j<=top;j++) o[dig[j]]++; o[0]=0; }
static int size(const int*c){ int s=0; for(int g=1;g<=9;g++) s+=c[g]; return s; }
static u64 nseeds=0; static int maxsteps=0;
static void fail(const char*why,const int*c0){ (void)why;(void)c0; longjmp(JB,1); }
static void run(const int*c0){ static u64 path[100000]; int np=0; int c[10]; memcpy(c,c0,sizeof c); int base;
  while(1){ for(int g=1;g<=9;g++) if(c[g]>127) fail("overflow",c0); u64 k=pack(c); u64 h=slot(k);
    if(stamp[h]==gen){ if(val[h]==-2) fail("cycle",c0); base=val[h]; break; }
    keys[h]=k; stamp[h]=gen; val[h]=-2; nkeys++; if(nkeys>(mask>>1)*1.6) fail("tablefull",c0); path[np++]=h;
    int s=size(c); if(s>maxsize) maxsize=s; if(s==0) fail("zero",c0);
    int o[10]; phi(c,o); memcpy(c,o,sizeof c); }
  for(int i=np-1;i>=0;i--){ base++; val[path[i]]=base; } if(base>maxsteps) maxsteps=base; nseeds++; }
static void rec(int g,int left,int*c){ if(g==0){ for(int t=0;t<=5;t++){ c[9]=t; if(size(c)) run(c); } return; } for(int k=0;k<=left;k++){ c[g]=k; rec(g-1,left-k,c); } c[g]=0; }

static int check(const int*a,const int*b,int*f,int*l0out){ for(int i=0;i<4;i++){ i64 pa=1,pb=1; for(int k=0;k<a[i];k++)pa*=10; for(int k=0;k<b[i];k++)pb*=10; C[i]=pa-pb; } PX=1;PY=1; for(int i=0;i<a[4];i++)PX*=10; for(int i=0;i<b[4];i++)PY*=10;
  int l0=0; int t[6]; for(t[0]=9;t[0]>=0;t[0]--)for(t[1]=t[0];t[1]>=0;t[1]--)for(t[2]=t[1];t[2]>=0;t[2]--)for(t[3]=t[2];t[3]>=0;t[3]--)for(t[4]=t[3];t[4]>=0;t[4]--){ if(t[0]==t[4]) continue; if(C[0]*t[0]+C[1]*t[1]+C[2]*t[2]+C[3]*t[3]-PY*t[4]+PX*t[4]==0) l0++; }
  *l0out=l0; if(l0) return 0;
  gen++; nkeys=0; nseeds=0; maxsteps=0; maxsize=0;
  if(setjmp(JB)) return 0;
  int c[10]={0},o[10]; c[1]=1; static u64 seen[4000]; int ns=0;
  while(1){ if(size(c)==0) return 0; for(int g=1;g<=9;g++) if(c[g]>127) return 0; u64 k=pack(c); for(int i=0;i<ns;i++) if(seen[i]==k) return 0; phi(c,o); if(!memcmp(o+1,c+1,9*sizeof(int))) break; if(ns>=4000) return 0; seen[ns++]=k; memcpy(c,o,sizeof c); }
  memcpy(f,c,10*sizeof(int)); f[0]=0; u64 h=slot(pack(f)); keys[h]=pack(f); stamp[h]=gen; val[h]=0; nkeys++; int cc[10]={0}; rec(8,15,cc); return 1; }
static int A[6],B[6],UA[6],UB[6]; static long idx=0; static int SH,NS; static long npass=0,nl0=0,ntot=0;
static void gb(int i){ if(i==5){ if(idx++%NS!=SH) return; ntot++; int f[10],l0; if(check(A,B,f,&l0)){ npass++; printf("PASS a="); for(int k=0;k<5;k++)printf("%d%s",A[k],k<4?",":""); printf(" b="); for(int k=0;k<5;k++)printf("%d%s",B[k],k<4?",":""); printf(" target="); for(int g=9;g>=1;g--) for(int q=0;q<f[g];q++) printf("%d",g); printf(" seeds=%llu states=%llu maxsteps=%d maxsize=%d\n",(unsigned long long)nseeds,(unsigned long long)nkeys,maxsteps,maxsize); fflush(stdout);} else if(l0) nl0++; return; }
  for(int p=0;p<5;p++){ if(UB[p]||p==A[i]) continue; UB[p]=1; B[i]=p; gb(i+1); UB[p]=0; } }
static void ga(int i){ if(i==5){ gb(0); return; } for(int p=0;p<5;p++){ if(UA[p]) continue; UA[p]=1; A[i]=p; ga(i+1); UA[p]=0; } }
int main(int argc,char**argv){ SH=atoi(argv[1]); NS=atoi(argv[2]); keys=calloc(mask+1,8); val=calloc(mask+1,2); stamp=calloc(mask+1,4); ga(0); printf("DONE shard=%d cores=%ld pass=%ld lemma0_fail=%ld\n",SH,ntot,npass,nl0); return 0; }
