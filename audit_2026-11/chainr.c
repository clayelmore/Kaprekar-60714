// Random-sampling version of chain.c for lengths where full rule enumeration is out of reach (d<=18).
// Samples rules that fix an arrangement of the target multiset and tests each by complete enumeration.
// usage: chainr d sortedDigitsDesc seed npairs assignsPerPair maxfind
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef int64_t i64; typedef uint64_t u64;
static int d; static int f[20]; static int fc[10];
static u64 binom[40][40]; static u64 P10[20];
static u64 N; static uint8_t *memo; static uint8_t (*cv)[10]; static u64 *adm; static u64 nadm; static u64 *near; static u64 nnear;
static u64 rs; static inline u64 rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline u64 rank_cnt(const uint8_t*cnt){ u64 r=0; int i=0; for(int g=0;g<10;g++) for(int k=0;k<cnt[g];k++){ r+=binom[g+i][i+1]; i++; } return r; }
static void rec(int dg,int left,uint8_t*cnt){ if(dg==0){ cnt[0]=left; u64 r=rank_cnt(cnt); memcpy(cv[r],cnt,10); int rep=0,nr=0; for(int g=0;g<10;g++){if(cnt[g]==d)rep=1; if(cnt[g]==d-1)nr=1;} if(!rep){ if(nr) near[nnear++]=r; else adm[nadm++]=r; } return; }
  for(int k=0;k<=left;k++){ cnt[dg]=k; rec(dg-1,left-k,cnt);} }
static i64 Cs[20]; static u64 Frank; static u64 path[65536]; static u64 gen=0; static uint32_t *stamp;
static inline u64 step(u64 r){ const uint8_t*cnt=cv[r]; i64 v=0; int pos=0,prev=-1; for(int g=9;g>=0;g--) if(cnt[g]){ if(prev>=0) v+=Cs[pos-1]*(prev-g); pos+=cnt[g]; prev=g; }
  u64 u=v<0?-v:v; uint8_t c2[10]={0}; for(int k=0;k<d;k++){ c2[u%10]++; u/=10; } return rank_cnt(c2); }
static inline int good(u64 r){ int n=0; u64 cur=r; int ok; while(1){ if(stamp[cur]==gen){ ok=(memo[cur]==1); break; } stamp[cur]=gen; memo[cur]=2; path[n++]=cur; cur=step(cur); } if(ok) for(int i=0;i<n;i++) memo[path[i]]=1; return ok; }
#define NK 48
static u64 killers[NK]; static int nk=0; static u64 *order;
static int test_rule(void){ gen++; stamp[Frank]=gen; memo[Frank]=1;
  for(int i=0;i<nk;i++) if(!good(killers[i])){ if(i){u64 t=killers[i]; memmove(killers+1,killers,i*sizeof(u64)); killers[0]=t;} return 0; }
  for(u64 i=0;i<nadm;i++) if(!good(order[i])){ if(nk<NK)nk++; memmove(killers+1,killers,(nk-1)*sizeof(u64)); killers[0]=order[i]; return 0; }
  int full=1; for(u64 i=0;i<nnear;i++) if(!good(near[i])){ full=0; break; } return 1+full; }
static int digs_ok(u64 v){ int c[10]={0}; for(int k=0;k<d;k++){ c[v%10]++; v/=10; } if(v) return 0; for(int g=0;g<10;g++) if(c[g]!=fc[g]) return 0; return 1; }
static u64 randarr(void){ int p[20]; memcpy(p,f,sizeof(int)*d); for(int i=d-1;i>0;i--){ int j=rnd()%(i+1); int t=p[i];p[i]=p[j];p[j]=t; } u64 v=0; for(int i=0;i<d;i++)v=v*10+p[i]; return v; }
int main(int argc,char**argv){ d=atoi(argv[1]); const char*s=argv[2]; rs=strtoull(argv[3],0,10)*0x9E3779B97F4A7C15ULL+88172645463325252ULL; u64 npairs=strtoull(argv[4],0,10); int per=atoi(argv[5]); int maxfind=atoi(argv[6]);
  for(int i=0;i<d;i++){ f[i]=s[i]-'0'; fc[f[i]]++; } P10[0]=1; for(int i=1;i<20;i++)P10[i]=P10[i-1]*10;
  for(int n=0;n<40;n++){binom[n][0]=1; for(int k=1;k<=n;k++)binom[n][k]=binom[n-1][k-1]+(k<=n-1?binom[n-1][k]:0);}
  N=binom[d+9][9]; memo=calloc(N,1); stamp=calloc(N,4); cv=calloc(N,10); adm=malloc(N*8); near=malloc(100*8); uint8_t cnt[10]; rec(9,d,cnt);
  order=malloc(nadm*8); memcpy(order,adm,nadm*8); for(u64 i=nadm-1;i>0;i--){ u64 j=rnd()%(i+1); u64 t=order[i];order[i]=order[j];order[j]=t; }
  { uint8_t c[10]; for(int g=0;g<10;g++)c[g]=fc[g]; Frank=rank_cnt(c); }
  int blk_start[10]; { int pos=0; for(int v=9;v>=0;v--) if(fc[v]){ blk_start[v]=pos; pos+=fc[v]; } }
  u64 tried=0,pairs=0,rules=0,found=0,fullc=0; int a[20],b[20];
  while(pairs<npairs && (int)found<maxfind){ u64 A=randarr(),R=randarr(); tried++; if(R>=A) continue; u64 B=A-R; if(!digs_ok(B)) continue; pairs++;
    int pa[10][20],pb[10][20],ca[10]={0},cb[10]={0}; u64 x=A,y=B; for(int k=0;k<d;k++){ int da=x%10, db=y%10; x/=10;y/=10; pa[da][ca[da]++]=k; pb[db][cb[db]++]=k; }
    for(int t=0;t<per;t++){ int ok=1;
      for(int v=0;v<10&&ok;v++){ int n=fc[v]; if(!n) continue; for(int i=n-1;i>0;i--){ int j=rnd()%(i+1); int q=pa[v][i];pa[v][i]=pa[v][j];pa[v][j]=q; j=rnd()%(i+1); q=pb[v][i];pb[v][i]=pb[v][j];pb[v][j]=q; }
        for(int i=0;i<n;i++){ a[blk_start[v]+i]=pa[v][i]; b[blk_start[v]+i]=pb[v][i]; if(pa[v][i]==pb[v][i]) ok=0; } }
      if(!ok) continue; i64 sm=0; for(int i=0;i<d;i++){ sm+=(i64)P10[a[i]]-(i64)P10[b[i]]; Cs[i]=sm; } rules++; int r=test_rule();
      if(r){ found++; if(r==2)fullc++; printf("UNIV %s F=%llu a=",r==2?"full":"strict",(unsigned long long)R); for(int i=0;i<d;i++)printf("%d%s",a[i],i<d-1?",":""); printf(" b="); for(int i=0;i<d;i++)printf("%d%s",b[i],i<d-1?",":""); printf("\n"); fflush(stdout); } } }
  printf("SUMMARY d=%d F=%s tried=%llu pairs=%llu rules=%llu universal=%llu full=%llu\n",d,s,(unsigned long long)tried,(unsigned long long)pairs,(unsigned long long)rules,(unsigned long long)found,(unsigned long long)fullc); return 0; }
