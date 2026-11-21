// Proof computation for the 146070 ladder (audit 2026-11).
// Phi acts on finite multisets N of NONZERO digits (sorted descending n_0>=n_1>=..., padded with zeros):
//   V = 990 n0 + 90000 n1 - 99990 n2 - 900 n3 - 99 n4 - n5 + sum_{j>=6} 10^j (n_{j-1} - n_j),  Phi(N) = nonzero digits of |V|.
// This IS the length-d rule on any state that has at least one zero digit.
// Seeds: every nonempty N with (#9 <= T9) and (#non-9 <= TR).  We follow every orbit and report:
// whether all reach {7,6,4,1}, the max number of steps, and the max multiset size ever visited.
// usage: closure T9 TR
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef uint64_t u64; typedef int64_t i64;
#define HB 27
static u64 *keys; static int16_t *val; static u64 mask=((u64)1<<HB)-1; static u64 nkeys=0;
static inline u64 pack(const int*c){ u64 k=0; for(int g=1;g<=9;g++){ if(c[g]>127){fprintf(stderr,"count overflow\n");exit(1);} k=(k<<7)|(u64)c[g]; } return k+1; }
static inline u64 slot(u64 k){ u64 h=(k*0x9E3779B97F4A7C15ULL)>>(64-HB); while(keys[h]&&keys[h]!=k) h=(h+1)&mask; return h; }
static int maxsize=0; static u64 maxsize_key=0;
static void phi(const int*c,int*o){ int n[256]; int k=0; for(int g=9;g>=1;g--) for(int i=0;i<c[g];i++) n[k++]=g; for(int i=k;i<k+8;i++) n[i]=0;
  i64 L=990LL*n[0]+90000LL*n[1]-99990LL*n[2]-900LL*n[3]-99LL*n[4]-n[5];
  int dig[260]; memset(dig,0,sizeof dig); int top=0; for(int j=6;j<=k;j++){ dig[j]=n[j-1]-n[j]; if(dig[j]) top=j; }
  memset(o,0,10*sizeof(int));
  if(top==0){ i64 v=L<0?-L:L; while(v){ o[v%10]++; v/=10; } o[0]=0; return; }
  i64 low; if(L>=0) low=L; else { low=1000000+L; int j=6; while(dig[j]==0){ dig[j]=9; j++; } dig[j]--; }
  if(low<0||low>=1000000){ fprintf(stderr,"low out of range\n"); exit(1); }
  for(int j=0;j<6;j++){ dig[j]=low%10; low/=10; }
  for(int j=0;j<=top;j++) o[dig[j]]++; o[0]=0; }
static int size(const int*c){ int s=0; for(int g=1;g<=9;g++) s+=c[g]; return s; }
static u64 nseeds=0, bad=0; static int maxsteps=0; static u64 hist[4096];
static void unpack(u64 k,int*c){ k--; for(int g=9;g>=1;g--){ c[g]=k&127; k>>=7; } c[0]=0; }
static void run(const int*c0){ static u64 path[100000]; int np=0; int c[10]; memcpy(c,c0,sizeof c); int base;
  while(1){ u64 k=pack(c); u64 h=slot(k);
    if(keys[h]){ if(val[h]==-2){ base=-1; break; } base=val[h]; break; }   // -2 = in progress => cycle
    keys[h]=k; val[h]=-2; nkeys++; if(nkeys>(mask>>1)){fprintf(stderr,"table full\n");exit(1);} path[np++]=h;
    int s=size(c); if(s>maxsize){ maxsize=s; maxsize_key=k; }
    if(s==0){ val[h]=-1; np--; base=-1; break; }                     // reached 0: failure
    int o[10]; phi(c,o); memcpy(c,o,sizeof c); }
  for(int i=np-1;i>=0;i--){ if(base>=0) base++; val[path[i]]=base<0?-1:base; }
  u64 h=slot(pack(c0)); int r=val[h]; nseeds++; if(r<0) bad++; else { if(r>maxsteps)maxsteps=r; hist[r]++; } }
static int T9,TR;
static void rec(int g,int left,int*c){ if(g==0){ for(int t=0;t<=T9;t++){ c[9]=t; if(size(c)) run(c); } return; } for(int k=0;k<=left;k++){ c[g]=k; rec(g-1,left-k,c); } c[g]=0; }
int main(int argc,char**argv){ T9=atoi(argv[1]); TR=atoi(argv[2]); keys=calloc(mask+1,8); val=calloc(mask+1,2);
  int f[10]={0}; f[7]=f[6]=f[4]=f[1]=1; u64 h=slot(pack(f)); keys[h]=pack(f); val[h]=0; nkeys++;
  { int o[10]; phi(f,o); if(memcmp(o,f,sizeof o)){ fprintf(stderr,"7641 not fixed\n"); return 1; } }
  int c[10]={0}; rec(8,TR,c);
  int mc[10]; unpack(maxsize_key,mc);
  printf("seeds=%llu (#9<=%d, #non9<=%d)  failures=%llu  states visited=%llu  max steps=%d  max multiset size visited=%d (counts 9..1:",(unsigned long long)nseeds,T9,TR,(unsigned long long)bad,(unsigned long long)nkeys,maxsteps,maxsize);
  for(int g=9;g>=1;g--) printf(" %d",mc[g]); printf(")\n"); return 0; }
