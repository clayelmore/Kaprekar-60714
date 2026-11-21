// Independent audit engine (2026-11). Classifies every digit multiset of length d
// under the rule n -> |sum_i c_i * s_i|, s = digits sorted descending.
// usage: kap d c0 c1 ... c_{d-1}   [-q]
// Output: one line per terminal (fixed point or cycle) with basin sizes.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef __int128 i128; typedef unsigned __int128 u128;
#define MAXD 40
static int d; static i128 C[MAXD]; // partial sums
static uint64_t binom[64][64];
static uint16_t *memo; static uint8_t *dist;
#define UNK 0
#define INPROG 0xFFFF
typedef struct { int len; u128 val; uint64_t rank; uint64_t basin, basin_strict; int maxsteps; } Term;
static Term terms[60000]; static int nterms=0;
static i128 parse(const char*s){int neg=0; if(*s=='-'){neg=1;s++;} else if(*s=='+')s++; i128 v=0; while(*s){v=v*10+(*s-'0');s++;} return neg?-v:v;}
static void pr(u128 v){char b[50];int n=0; if(v==0){printf("0");return;} while(v){b[n++]='0'+(int)(v%10);v/=10;} while(n--)putchar(b[n]);}
static inline uint64_t rank_cnt(const int*cnt){ // ascending sequence a_i, rank=sum C(a_i+i,i+1)
  uint64_t r=0; int i=0; for(int dg=0;dg<10;dg++){ for(int k=0;k<cnt[dg];k++){ r+=binom[dg+i][i+1]; i++; } } return r; }
static inline u128 stepval(const int*cnt){ // value = sum_j C_j * gap_j
  i128 v=0; int pos=0; int prev=-1; 
  for(int dg=9;dg>=0;dg--){ if(cnt[dg]){ if(prev>=0) v+=C[pos-1]*(prev-dg); pos+=cnt[dg]; prev=dg; } }
  return v<0?(u128)(-v):(u128)v; }
static inline void digits(u128 v,int*cnt){ memset(cnt,0,10*sizeof(int)); int n=0;
  uint64_t lo=(uint64_t)(v%(u128)10000000000000000ULL); u128 hi=v/(u128)10000000000000000ULL;
  int k; for(k=0;k<16&&n<d;k++){cnt[lo%10]++;lo/=10;n++;}
  if(n<d){ uint64_t mid=(uint64_t)(hi%(u128)10000000000000000ULL); uint64_t top=(uint64_t)(hi/(u128)10000000000000000ULL);
    for(k=0;k<16&&n<d;k++){cnt[mid%10]++;mid/=10;n++;}
    while(n<d){cnt[top%10]++;top/=10;n++;} } }
static uint64_t pathr[100000]; static u128 pathv[100000];
static uint64_t nstates=0;
static void process(const int*cnt0){
  uint64_t r=rank_cnt(cnt0); int isrep=0,isnear=0; for(int g=0;g<10;g++){ if(cnt0[g]==d)isrep=1; if(cnt0[g]==d-1)isnear=1; }
  int cnt[10]; memcpy(cnt,cnt0,sizeof cnt); int n=0; uint64_t cur=r; int t; int base;
  while(1){
    uint16_t m=memo[cur];
    if(m==INPROG){ // new cycle: find start
      int s=n-1; while(pathr[s]!=cur)s--; int len=n-s; t=nterms++; if(nterms>=60000){fprintf(stderr,"too many terminals\n");exit(1);}
      terms[t].len=len; terms[t].val=pathv[s]; terms[t].rank=cur; terms[t].basin=terms[t].basin_strict=0; terms[t].maxsteps=0;
      for(int i=s;i<n;i++){ memo[pathr[i]]=(uint16_t)(t+1); dist[pathr[i]]=0; }
      n=s; base=0; break; }
    if(m!=UNK){ t=m-1; base=dist[cur]; break; }
    memo[cur]=INPROG; u128 v=stepval(cnt); pathr[n]=cur; pathv[n]=v; n++;
    digits(v,cnt); cur=rank_cnt(cnt);
  }
  for(int i=n-1;i>=0;i--){ base++; memo[pathr[i]]=(uint16_t)(t+1); dist[pathr[i]]=base>255?255:base; }
  // pathv[i] is value of image of path state i; for a fixed point, val = image value. 
  (void)isnear;
}
static uint8_t *flag; // bit0 rep, bit1 near
static void rec(int dg,int left,int*cnt){
  if(dg==0){ cnt[0]=left; process(cnt); uint64_t r=rank_cnt(cnt); int f=0; for(int g=0;g<10;g++){ if(cnt[g]==d)f|=1; if(cnt[g]==d-1)f|=2; } flag[r>>0]=f; nstates++; return; }
  for(int k=0;k<=left;k++){ cnt[dg]=k; rec(dg-1,left-k,cnt); } }
int main(int argc,char**argv){
  d=atoi(argv[1]); if(argc<2+d){fprintf(stderr,"need %d coefs\n",d);return 1;}
  i128 s=0; for(int i=0;i<d;i++){ s+=parse(argv[2+i]); C[i]=s; } if(s!=0){fprintf(stderr,"coefs do not sum to zero\n");return 1;}
  for(int n=0;n<64;n++){binom[n][0]=1; for(int k=1;k<=n;k++)binom[n][k]=binom[n-1][k-1]+(k<=n-1?binom[n-1][k]:0);}
  uint64_t N=binom[d+9][9]; memo=calloc(N,2); dist=calloc(N,1); flag=calloc(N,1);
  int cnt[10]; rec(9,d,cnt);
  // tally
  uint64_t tot=0,tots=0;
  for(uint64_t r=0;r<N;r++){ int t=memo[r]-1; if(!(flag[r]&1)){ terms[t].basin++; tot++; if(dist[r]>terms[t].maxsteps)terms[t].maxsteps=dist[r]; if(!(flag[r]&2)){terms[t].basin_strict++; tots++;} } }
  printf("d=%d states=%llu nonrep=%llu strict=%llu terminals=%d\n",d,(unsigned long long)N,(unsigned long long)tot,(unsigned long long)tots,nterms);
  int shown=0;
  for(int t=0;t<nterms;t++){ if(terms[t].basin==0 && terms[t].val!=0) continue; if(shown++>=40){printf("  ...\n");break;}
    printf("  %s len=%d val=",terms[t].len==1?"FIX":"CYC",terms[t].len); pr(terms[t].val);
    printf(" basin=%llu strict=%llu maxsteps=%d\n",(unsigned long long)terms[t].basin,(unsigned long long)terms[t].basin_strict,terms[t].maxsteps); }
  return 0; }
