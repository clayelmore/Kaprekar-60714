// Complete check that one rule sends every non-repdigit L-digit multiset to F, base 10 (2026-11-21).
// usage: univcheck L F a0,a1,..  b0,b1,..   (letter i, sorted descending, sits at place a_i in word 1, b_i in word 2)
// prints PASS or FAIL.   Build: cc -O2 -o univcheck univcheck.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef int64_t i64; typedef uint64_t u64;
static int L; static i64 c[32],F; static u64 binom[64][64]; static uint8_t *st; static u64 *path;
static u64 rank_cnt(const int*cnt){ u64 r=0; int i=0; for(int dg=0;dg<10;dg++) for(int k=0;k<cnt[dg];k++){ r+=binom[dg+i][i+1]; i++; } return r; }
static i64 val(const int*cnt){ i64 v=0; int i=0; for(int dg=9;dg>=0;dg--) for(int k=0;k<cnt[dg];k++) v+=c[i++]*dg; return v<0?-v:v; }
static int fail=0;
static void proc(const int*cnt0){ for(int g=0;g<10;g++) if(cnt0[g]==L) return; int cnt[10]; memcpy(cnt,cnt0,sizeof cnt); int n=0; u64 cur=rank_cnt(cnt);
  while(st[cur]==0){ st[cur]=2; path[n++]=cur; i64 v=val(cnt); if(v==0){ fail=1; return; }
    int nx[10]={0}; i64 w=v; for(int k=0;k<L;k++){ nx[w%10]++; w/=10; } u64 r=rank_cnt(nx);
    if(r==cur){ if(v!=F){ fail=1; return; } break; }
    if(st[r]==2){ fail=1; return; }
    memcpy(cnt,nx,sizeof cnt); cur=r; }
  for(int i=0;i<n;i++) st[path[i]]=1; }
static void rec(int dg,int left,int*cnt){ if(fail) return; if(dg==0){ cnt[0]=left; proc(cnt); return; } for(int k=0;k<=left;k++){ cnt[dg]=k; rec(dg-1,left-k,cnt); } }
int main(int argc,char**argv){ L=atoi(argv[1]); F=atoll(argv[2]); i64 p10[32]; p10[0]=1; for(int i=1;i<32&&i<19;i++) p10[i]=p10[i-1]*10;
  char*p=argv[3]; char*q=argv[4]; for(int i=0;i<L;i++){ int a=strtol(p,&p,10); p++; int b=strtol(q,&q,10); q++; c[i]=p10[a]-p10[b]; }
  for(int n=0;n<64;n++){ binom[n][0]=1; for(int k=1;k<=n;k++) binom[n][k]=binom[n-1][k-1]+(k<=n-1?binom[n-1][k]:0); }
  u64 N=binom[L+9][9]; st=calloc(N,1); path=malloc(N*8); int cnt[10]; rec(9,L,cnt); puts(fail?"FAIL":"PASS"); return 0; }
