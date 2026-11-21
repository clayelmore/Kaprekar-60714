// Half-swap rules at length d = 2n in base B (2026-11-21).  Build: cc -O2 -DB=10 -DNH=3 -o hs halfswap.c
// A half-swap rule moves every letter exactly n places: for each low place q in 0..n-1 one letter P_q sits at
// place q+n in word 1 and place q in word 2, and one letter M_q the other way round.  Then
//   K(s) = (B^n - 1) * | sum_q B^q (s[P_q] - s[M_q]) |.
// Enumerates all (2n)! rules, tests each by complete enumeration at length 2n (no extension), prints the
// universal ones as  q=n-1..0 pairs "P-M"  with the endpoint.   usage: hs [shard nshards]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <setjmp.h>
#ifndef B
#define B 10
#endif
#ifndef NH
#define NH 3
#endif
#define D (2*NH)
typedef uint64_t u64; typedef int64_t i64;
static jmp_buf JA; static u64 binom[80][80]; static uint32_t *stA; static uint32_t genA=0; static i64 CS[40]; static int haveF; static i64 FA; static int maxst;
static inline u64 rank_cnt(const int*cnt){ u64 r=0; int i=0; for(int dg=0;dg<B;dg++){ for(int k=0;k<cnt[dg];k++){ r+=binom[dg+i][i+1]; i++; } } return r; }
static inline i64 stepval(const int*cnt){ i64 v=0; int pos=0; int prev=-1; for(int dg=B-1;dg>=0;dg--){ if(cnt[dg]){ if(prev>=0) v+=CS[pos-1]*(prev-dg); pos+=cnt[dg]; prev=dg; } } return v<0?-v:v; }
static void procA(const int*cnt0){ for(int g=0;g<B;g++) if(cnt0[g]==D) return;
  int cnt[B]; memcpy(cnt,cnt0,sizeof cnt); static u64 path[8192]; int n=0; u64 cur=rank_cnt(cnt); i64 v=0;
  while(1){ uint32_t m=stA[cur]; if(m==genA) break; if(m==genA+1){ if(haveF||path[n-1]!=cur) longjmp(JA,1); haveF=1; FA=v; break; }
    stA[cur]=genA+1; path[n++]=cur; if(n>=8192) longjmp(JA,1); v=stepval(cnt); if(v==0) longjmp(JA,1);
    memset(cnt,0,sizeof cnt); i64 w=v; for(int k=0;k<D;k++){ cnt[w%B]++; w/=B; } cur=rank_cnt(cnt); }
  if(n>maxst) maxst=n; for(int i=0;i<n;i++) stA[path[i]]=genA; }
static void recA(int dg,int left,int*cnt){ if(dg==0){ cnt[0]=left; procA(cnt); return; } for(int k=0;k<=left;k++){ cnt[dg]=k; recA(dg-1,left-k,cnt); } }
static i64 pw[40]; static int slot[D]; static int used[D]; static long idx=0,ntot=0,nuniv=0; static int SH=0,NS=1;
static const char DG[]="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
static void prbase(i64 v){ char buf[70]; int n=0; if(v==0){ putchar('0'); return; } while(v){ buf[n++]=DG[v%B]; v/=B; } while(n--) putchar(buf[n]); }
static void test(void){ if(idx++%NS!=SH) return; ntot++;
  i64 c[D]; for(int t=0;t<D;t++){ int q=t/2; i64 w=pw[q+NH]-pw[q]; c[slot[t]]=(t%2==0)?w:-w; }
  i64 s=0; for(int i=0;i<D;i++){ s+=c[i]; CS[i]=s; }
  genA+=2; haveF=0; FA=0; maxst=0; if(setjmp(JA)) return; int cnt[B]; recA(B-1,D,cnt); if(!haveF) return;
  nuniv++; printf("UNIV base=%d n=%d pairs=",B,NH); for(int q=NH-1;q>=0;q--) printf("%c-%c%s",'A'+slot[2*q],'A'+slot[2*q+1],q?",":""); printf(" endpoint="); prbase(FA); printf(" m="); prbase(FA/(pw[NH]-1)); printf(" maxsteps=%d\n",maxst); }
static void gen(int t){ if(t==D){ test(); return; } for(int i=0;i<D;i++){ if(used[i]) continue; used[i]=1; slot[t]=i; gen(t+1); used[i]=0; } }
int main(int argc,char**argv){
  if(argc>2 && !strcmp(argv[1],"one")){ // usage: hs one P-M,P-M,...  (letter indices, place n-1 first)
    pw[0]=1; for(int i=1;i<40;i++) pw[i]=pw[i-1]*B;
    for(int n=0;n<80;n++){binom[n][0]=1; for(int k=1;k<=n;k++)binom[n][k]=binom[n-1][k-1]+(k<=n-1?binom[n-1][k]:0);}
    stA=calloc(binom[D+B-1][B-1],4); char*p=argv[2];
    for(int q=NH-1;q>=0;q--){ slot[2*q]=strtol(p,&p,10); p++; slot[2*q+1]=strtol(p,&p,10); p++; }
    i64 c[D]; for(int t=0;t<D;t++){ int q=t/2; i64 w=pw[q+NH]-pw[q]; c[slot[t]]=(t%2==0)?w:-w; }
    i64 s=0; for(int i=0;i<D;i++){ s+=c[i]; CS[i]=s; }
    genA=2; haveF=0; FA=0; maxst=0; int ok=0; if(!setjmp(JA)){ int cnt[B]; recA(B-1,D,cnt); ok=haveF; }
    printf("base=%d len=%d ",B,D); if(ok){ printf("UNIVERSAL endpoint="); prbase(FA); printf(" m="); prbase(FA/(pw[NH]-1)); printf("\n"); } else printf("FAIL\n"); return 0; }
  if(argc>2){ SH=atoi(argv[1]); NS=atoi(argv[2]); }
  pw[0]=1; for(int i=1;i<40;i++) pw[i]=pw[i-1]*B;
  for(int n=0;n<80;n++){binom[n][0]=1; for(int k=1;k<=n;k++)binom[n][k]=binom[n-1][k-1]+(k<=n-1?binom[n-1][k]:0);}
  stA=calloc(binom[D+B-1][B-1],4); gen(0);
  printf("DONE base=%d n=%d shard=%d rules=%ld universal=%ld\n",B,NH,SH,ntot,nuniv); return 0; }
