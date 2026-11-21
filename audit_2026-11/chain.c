// Unified-chain search (audit 2026-11): for a target digit multiset F at length d, enumerate EVERY
// full-variable rule (pair of place-bijections a,b; c_i = 10^a_i - 10^b_i) that fixes some arrangement
// of F, and test universality by complete enumeration of all digit multisets.
// usage: chain d sortedDigitsDesc shard nshards     e.g. chain 9 776644110 0 16
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef int64_t i64; typedef uint64_t u64;
static int d; static int f[20]; static int fc[10];
static u64 binom[40][40]; static u64 P10[20];
static u64 N; static uint8_t *memo; static uint8_t (*cv)[10]; static u64 *adm; static u64 nadm; static u64 *near; static u64 nnear;
static inline u64 rank_cnt(const uint8_t*cnt){ u64 r=0; int i=0; for(int g=0;g<10;g++) for(int k=0;k<cnt[g];k++){ r+=binom[g+i][i+1]; i++; } return r; }
static void rec(int dg,int left,uint8_t*cnt){ if(dg==0){ cnt[0]=left; u64 r=rank_cnt(cnt); memcpy(cv[r],cnt,10); int rep=0,nr=0; for(int g=0;g<10;g++){if(cnt[g]==d)rep=1; if(cnt[g]==d-1)nr=1;} if(!rep){ if(nr) near[nnear++]=r; else adm[nadm++]=r; } return; }
  for(int k=0;k<=left;k++){ cnt[dg]=k; rec(dg-1,left-k,cnt);} }
static i64 Cs[20]; static u64 Frank;
static u64 path[4096];
static u64 gen=0; static uint32_t *stamp; // per-rule generation stamps avoid memset
static inline u64 step(u64 r){ const uint8_t*cnt=cv[r]; i64 v=0; int pos=0,prev=-1; for(int g=9;g>=0;g--) if(cnt[g]){ if(prev>=0) v+=Cs[pos-1]*(prev-g); pos+=cnt[g]; prev=g; }
  u64 u=v<0?-v:v; uint8_t c2[10]={0}; for(int k=0;k<d;k++){ c2[u%10]++; u/=10; } return rank_cnt(c2); }
// returns 1 if orbit of r reaches F; memo values valid only if stamp==gen: 1 good, 2 inprogress
static inline int good(u64 r){ int n=0; u64 cur=r; int ok;
  while(1){ if(stamp[cur]==gen){ ok=(memo[cur]==1); break; } stamp[cur]=gen; memo[cur]=2; path[n++]=cur; cur=step(cur); }
  if(ok) for(int i=0;i<n;i++) memo[path[i]]=1; return ok; }
#define NK 24
static u64 killers[NK]; static int nk=0;
static int test_rule(void){ gen++; stamp[Frank]=gen; memo[Frank]=1;
  for(int i=0;i<nk;i++) if(!good(killers[i])){ if(i){u64 t=killers[i]; memmove(killers+1,killers,i*sizeof(u64)); killers[0]=t;} return 0; }
  for(u64 i=0;i<nadm;i++) if(!good(adm[i])){ if(nk<NK)nk++; memmove(killers+1,killers,(nk-1)*sizeof(u64)); killers[0]=adm[i]; return 0; }
  int full=1; for(u64 i=0;i<nnear;i++) if(!good(near[i])){ full=0; break; }
  return 1+full; }
static int digs_ok(u64 v){ int c[10]={0}; for(int k=0;k<d;k++){ c[v%10]++; v/=10; } if(v) return 0; for(int g=0;g<10;g++) if(c[g]!=fc[g]) return 0; return 1; }
static u64 *arr; static u64 narr=0;
static u64 npairs=0,nrules=0,nuniv=0,nfull=0;
static int a[20],b[20]; static u64 curR;
static int blk_start[10], blk_len[10]; static int pa[10][20], pb[10][20]; // places of digit v in A,B
static int vals[10], nvals;
static void emit(int kind){ printf("UNIV %s F=%llu a=", kind==2?"full":"strict",(unsigned long long)curR); for(int i=0;i<d;i++)printf("%d%s",a[i],i<d-1?",":""); printf(" b="); for(int i=0;i<d;i++)printf("%d%s",b[i],i<d-1?",":""); printf("\n"); }
static void permB(int vi); 
static int usedA[20],usedB[20];
static void assign(int vi,int k,int side){ // assign k-th rank of block vi
  int v=vals[vi]; int len=blk_len[v];
  if(k==len){ if(side==0) assign(vi,0,1); else { if(vi+1<nvals) assign(vi+1,0,0); else { // complete
        i64 s=0; for(int i=0;i<d;i++){ s+=(i64)P10[a[i]]-(i64)P10[b[i]]; Cs[i]=s; } nrules++; int r=test_rule(); if(r){ nuniv++; if(r==2)nfull++; emit(r);} } } return; }
  int rk=blk_start[v]+k; int*pl= side==0?pa[v]:pb[v]; int*used= side==0?usedA:usedB;
  for(int j=0;j<len;j++){ int p=pl[j]; if(used[p]) continue; if(side==1 && a[rk]==p) continue; used[p]=1; if(side==0)a[rk]=p; else b[rk]=p; assign(vi,k+1,side); used[p]=0; } }
int main(int argc,char**argv){ d=atoi(argv[1]); const char*s=argv[2]; int shard=atoi(argv[3]),ns=atoi(argv[4]);
  for(int i=0;i<d;i++){ f[i]=s[i]-'0'; fc[f[i]]++; } P10[0]=1; for(int i=1;i<20;i++)P10[i]=P10[i-1]*10;
  for(int n=0;n<40;n++){binom[n][0]=1; for(int k=1;k<=n;k++)binom[n][k]=binom[n-1][k-1]+(k<=n-1?binom[n-1][k]:0);}
  N=binom[d+9][9]; memo=calloc(N,1); stamp=calloc(N,4); cv=calloc(N,10); adm=malloc(N*8); near=malloc(100*8); uint8_t cnt[10]; rec(9,d,cnt);
  { uint8_t c[10]; for(int g=0;g<10;g++)c[g]=fc[g]; Frank=rank_cnt(c); }
  nvals=0; { int pos=0; for(int v=9;v>=0;v--) if(fc[v]){ vals[nvals++]=v; blk_start[v]=pos; blk_len[v]=fc[v]; pos+=fc[v]; } }
  // all arrangements (ascending digit array, next_permutation)
  u64 cap=1; { u64 fact=1; for(int i=2;i<=d;i++)fact*=i; cap=fact; for(int g=0;g<10;g++){ u64 q=1; for(int i=2;i<=fc[g];i++)q*=i; cap/=q; } }
  arr=malloc(cap*8); int p[20]; for(int i=0;i<d;i++)p[i]=f[d-1-i];
  while(1){ u64 v=0; for(int i=0;i<d;i++)v=v*10+p[i]; arr[narr++]=v; int i=d-2; while(i>=0&&p[i]>=p[i+1])i--; if(i<0)break; int j=d-1; while(p[j]<=p[i])j--; int t=p[i];p[i]=p[j];p[j]=t; for(int x=i+1,y=d-1;x<y;x++,y--){t=p[x];p[x]=p[y];p[y]=t;} }
  for(u64 ia=shard; ia<narr; ia+=ns){ u64 A=arr[ia];
    for(u64 ir=0; ir<narr; ir++){ u64 R=arr[ir]; if(R>=A) break; u64 B=A-R; if(!digs_ok(B)) continue; npairs++; curR=R;
      int ca[10]={0},cb[10]={0}; u64 x=A,y=B; for(int k=0;k<d;k++){ int da=x%10, db=y%10; x/=10;y/=10; pa[da][ca[da]++]=k; pb[db][cb[db]++]=k; }
      memset(usedA,0,sizeof usedA); memset(usedB,0,sizeof usedB); assign(0,0,0); } }
  printf("SUMMARY d=%d F=%s shard=%d/%d arrangements=%llu pairs=%llu rules=%llu universal_strict=%llu universal_full=%llu\n",d,s,shard,ns,(unsigned long long)narr,(unsigned long long)npairs,(unsigned long long)nrules,(unsigned long long)nuniv,(unsigned long long)nfull);
  return 0; }
