// Audit census: all full-variable rules at length d (d<=7), universal fixed points under the strict
// convention (start states: neither repdigit nor near-repdigit). Also counts collapse rules and all-rule universals.
// usage: census d [all]   ("all" = include non-full-variable rules)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef int64_t i64; typedef uint64_t u64;
static int d; static u64 binom[40][40]; static u64 P10[12];
static u64 N; static uint8_t *memo; static uint32_t *stamp; static uint32_t gen; static uint8_t (*cv)[10]; static u64 *adm; static u64 nadm; static u64 *near; static u64 nnear;
static i64 Cs[12];
static inline u64 rank_cnt(const uint8_t*cnt){ u64 r=0; int i=0; for(int g=0;g<10;g++) for(int k=0;k<cnt[g];k++){ r+=binom[g+i][i+1]; i++; } return r; }
static void rec(int dg,int left,uint8_t*cnt){ if(dg==0){ cnt[0]=left; u64 r=rank_cnt(cnt); memcpy(cv[r],cnt,10); int rep=0,nr=0; for(int g=0;g<10;g++){if(cnt[g]==d)rep=1; if(cnt[g]==d-1)nr=1;} if(!rep){ if(nr) near[nnear++]=r; else adm[nadm++]=r; } return; }
  for(int k=0;k<=left;k++){ cnt[dg]=k; rec(dg-1,left-k,cnt);} }
static u64 lastval;
static inline u64 step(u64 r){ const uint8_t*cnt=cv[r]; i64 v=0; int pos=0,prev=-1; for(int g=9;g>=0;g--) if(cnt[g]){ if(prev>=0) v+=Cs[pos-1]*(prev-g); pos+=cnt[g]; prev=g; }
  u64 u=v<0?-v:v; lastval=u; uint8_t c2[10]={0}; for(int k=0;k<d;k++){ c2[u%10]++; u/=10; } return rank_cnt(c2); }
static u64 path[4096];
static inline int good(u64 r){ int n=0; u64 cur=r; int ok; while(1){ if(stamp[cur]==gen){ ok=(memo[cur]==1); break; } stamp[cur]=gen; memo[cur]=2; path[n++]=cur; cur=step(cur); } if(ok) for(int i=0;i<n;i++) memo[path[i]]=1; return ok; }
static int a[12],b[12];
static u64 *ufp; static u64 nufp=0; static u64 nrules=0,nuniv=0,ncollapse=0,nfullnear=0;
static void test(void){ nrules++; gen++; // terminal of first admissible state
  u64 cur=adm[0]; int n=0; while(stamp[cur]!=gen){ stamp[cur]=gen; memo[cur]=2; path[n++]=cur; cur=step(cur); }
  u64 nx=step(cur); u64 F=lastval; if(nx!=cur){ return; } // cycle
  // cur is a fixed multiset with value F
  gen++; stamp[cur]=gen; memo[cur]=1; for(u64 i=0;i<nadm;i++) if(!good(adm[i])) return;
  if(F==0){ ncollapse++; return; }
  nuniv++; if(getenv("PRINT")){ printf("UNIV F=%llu a=",(unsigned long long)F); for(int k=0;k<d;k++)printf("%d%s",a[k],k<d-1?",":""); printf(" b="); for(int k=0;k<d;k++)printf("%d%s",b[k],k<d-1?",":""); printf("\n"); } int full=1; for(u64 i=0;i<nnear;i++) if(!good(near[i])){full=0;break;} nfullnear+=full; ufp[nufp++]=F; }
static int ua[12],ub[12]; static int allrules=0;
static void gb(int i){ if(i==d){ int same=1; for(int k=0;k<d;k++) if(a[k]!=b[k])same=0; if(same) return; i64 s=0; for(int k=0;k<d;k++){ s+=(i64)P10[a[k]]-(i64)P10[b[k]]; Cs[k]=s; } test(); return; }
  for(int p=0;p<d;p++){ if(ub[p]) continue; if(!allrules && p==a[i]) continue; ub[p]=1; b[i]=p; gb(i+1); ub[p]=0; } }
static void ga(int i){ if(i==d){ gb(0); return; } for(int p=0;p<d;p++){ if(ua[p]) continue; ua[p]=1; a[i]=p; ga(i+1); ua[p]=0; } }
static int cmp(const void*x,const void*y){ u64 A=*(u64*)x,B=*(u64*)y; return A<B?-1:A>B; }
int main(int argc,char**argv){ d=atoi(argv[1]); allrules=argc>2; P10[0]=1; for(int i=1;i<12;i++)P10[i]=P10[i-1]*10;
  for(int n=0;n<40;n++){binom[n][0]=1; for(int k=1;k<=n;k++)binom[n][k]=binom[n-1][k-1]+(k<=n-1?binom[n-1][k]:0);}
  N=binom[d+9][9]; memo=calloc(N,1); stamp=calloc(N,4); cv=calloc(N,10); adm=malloc(N*8); near=malloc(100*8); ufp=malloc(8*20000000); uint8_t cnt[10]; rec(9,d,cnt);
  ga(0); qsort(ufp,nufp,8,cmp); u64 nd=0; for(u64 i=0;i<nufp;i++) if(i==0||ufp[i]!=ufp[i-1]) nd++;
  printf("d=%d rules=%llu admissible=%llu universal_rules=%llu (also from near-repdigits: %llu) collapse_rules=%llu distinct_universal_fixed_points=%llu\n",d,(unsigned long long)nrules,(unsigned long long)nadm,(unsigned long long)nuniv,(unsigned long long)nfullnear,(unsigned long long)ncollapse,(unsigned long long)nd);
  FILE*o; char fn[64]; sprintf(fn,"census_d%d%s.txt",d,allrules?"_all":""); o=fopen(fn,"w"); for(u64 i=0;i<nufp;i++) if(i==0||ufp[i]!=ufp[i-1]) fprintf(o,"%llu\n",(unsigned long long)ufp[i]); fclose(o); return 0; }
