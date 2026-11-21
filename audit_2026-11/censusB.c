// Census of N-letter cores in base B (2026-11-21).  Build: cc -O2 -DN=6 -DB=8 -o cb censusB.c
// Same two tests as censusN.c, with 10 replaced by B everywhere:
//   K(s) = | sum_{k=N}^{d-1} B^k (s_{k-1}-s_k) + sum_{i<N-1} c_i s_i - B^y s_{N-1} + B^x s_{d-1} |, c_i = B^a_i - B^b_i.
//   A: complete enumeration at length AD (default N+6).   B-test: Lemma 0 + closure of all seeds
//   (#top digit <= N-1, other nonzero digits <= B-1+N) under the length-free map Phi.
// usage: cb shard nshards [AD]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <setjmp.h>
#ifndef N
#define N 6
#endif
#ifndef B
#define B 10
#endif
#if B<=10
#define BITS 7
#else
#define BITS 5
#endif
#define LIM ((1<<BITS)-1)
typedef uint64_t u64; typedef int64_t i64;
static jmp_buf JB,JA; static uint32_t *stamp; static uint32_t gen=1;
#define HB 24
static u64 *keys; static int16_t *val; static u64 mask=((u64)1<<HB)-1; static u64 nkeys=0;
static i64 C[N],PX,PY,PBN;
static inline u64 pack(const int*c){ u64 k=0; for(int g=1;g<B;g++) k=(k<<BITS)|(u64)c[g]; return k+1; }
static inline u64 slot(u64 k){ u64 h=(k*0x9E3779B97F4A7C15ULL)>>(64-HB); while(stamp[h]==gen&&keys[h]!=k) h=(h+1)&mask; return h; }
static int maxsize=0;
static void phi(const int*c,int*o){ int n[300]; int k=0; for(int g=B-1;g>=1;g--) for(int i=0;i<c[g];i++){ if(k>=200) longjmp(JB,1); n[k++]=g; }
  for(int i=k;i<k+N+2;i++) n[i]=0;
  i64 L=-PY*n[N-1]; for(int i=0;i<N-1;i++) L+=C[i]*n[i];
  int dig[300]; memset(dig,0,sizeof dig); int top=0; for(int j=N;j<=k;j++){ dig[j]=n[j-1]-n[j]; if(dig[j]) top=j; }
  memset(o,0,B*sizeof(int));
  if(top==0){ i64 v=L<0?-L:L; while(v){ o[v%B]++; v/=B; } o[0]=0; return; }
  i64 low; if(L>=0) low=L; else { low=PBN+L; int j=N; while(dig[j]==0){ dig[j]=B-1; j++; } dig[j]--; }
  if(low<0||low>=PBN){ longjmp(JB,1); }
  for(int j=0;j<N;j++){ dig[j]=low%B; low/=B; }
  for(int j=0;j<=top;j++) o[dig[j]]++; o[0]=0; }
static int size(const int*c){ int s=0; for(int g=1;g<B;g++) s+=c[g]; return s; }
static u64 nseeds=0; static int maxsteps=0;
static void run(const int*c0){ static u64 path[100000]; int np=0; int c[B]; memcpy(c,c0,sizeof c); int base;
  while(1){ for(int g=1;g<B;g++) if(c[g]>LIM) longjmp(JB,1); u64 k=pack(c); u64 h=slot(k);
    if(stamp[h]==gen){ if(val[h]==-2) longjmp(JB,1); base=val[h]; break; }
    keys[h]=k; stamp[h]=gen; val[h]=-2; nkeys++; if(nkeys>(mask>>1)*1.6||np>=99999) longjmp(JB,1); path[np++]=h;
    int s=size(c); if(s>maxsize) maxsize=s; if(s==0) longjmp(JB,1);
    int o[B]; phi(c,o); memcpy(c,o,sizeof c); }
  for(int i=np-1;i>=0;i--){ base++; val[path[i]]=base; } if(base>maxsteps) maxsteps=base; nseeds++; }
static void rec(int g,int left,int*c){ if(g==0){ for(int t=0;t<=N-1;t++){ c[B-1]=t; if(size(c)) run(c); } c[B-1]=0; return; } for(int k=0;k<=left;k++){ c[g]=k; rec(g-1,left-k,c); } c[g]=0; }
static int l0bad; static int T0[N];
static void lem0(int i,int hi){ if(l0bad) return; if(i==N){ if(T0[0]==T0[N-1]) return; i64 v=(PX-PY)*T0[N-1]; for(int k=0;k<N-1;k++) v+=C[k]*T0[k]; if(v==0) l0bad=1; return; }
  for(int t=hi;t>=0;t--){ T0[i]=t; lem0(i+1,t); } }
static i64 ipow(int e){ i64 p=1; for(int k=0;k<e;k++) p*=B; return p; }
static int checkB(const int*a,const int*b,int*f){ for(int i=0;i<N-1;i++) C[i]=ipow(a[i])-ipow(b[i]);
  PX=ipow(a[N-1]); PY=ipow(b[N-1]); PBN=ipow(N);
  gen++; nkeys=0; nseeds=0; maxsteps=0; maxsize=0;
  if(setjmp(JB)) return 0;
  int c[B],o[B]; memset(c,0,sizeof c); c[1]=1; static u64 seen[4000]; int ns=0;
  while(1){ if(size(c)==0) return 0; for(int g=1;g<B;g++) if(c[g]>LIM) return 0; u64 k=pack(c); for(int i=0;i<ns;i++) if(seen[i]==k) return 0; phi(c,o); if(!memcmp(o+1,c+1,(B-1)*sizeof(int))) break; if(ns>=4000) return 0; seen[ns++]=k; memcpy(c,o,sizeof c); }
  l0bad=0; lem0(0,B-1); if(l0bad) return 0;
  memcpy(f,c,B*sizeof(int)); f[0]=0; u64 h=slot(pack(f)); keys[h]=pack(f); stamp[h]=gen; val[h]=0; nkeys++; int cc[B]; memset(cc,0,sizeof cc); rec(B-2,B-1+N,cc); return 1; }
// ---------- test A ----------
static int AD; static u64 binom[80][80]; static uint32_t *stA; static uint32_t genA=0; static i64 CS[40]; static int haveF; static i64 FA;
static inline u64 rank_cnt(const int*cnt){ u64 r=0; int i=0; for(int dg=0;dg<B;dg++){ for(int k=0;k<cnt[dg];k++){ r+=binom[dg+i][i+1]; i++; } } return r; }
static inline i64 stepval(const int*cnt){ i64 v=0; int pos=0; int prev=-1; for(int dg=B-1;dg>=0;dg--){ if(cnt[dg]){ if(prev>=0) v+=CS[pos-1]*(prev-dg); pos+=cnt[dg]; prev=dg; } } return v<0?-v:v; }
static void procA(const int*cnt0){ for(int g=0;g<B;g++) if(cnt0[g]==AD) return;
  int cnt[B]; memcpy(cnt,cnt0,sizeof cnt); static u64 path[8192]; int n=0; u64 cur=rank_cnt(cnt); i64 v=0;
  while(1){ uint32_t m=stA[cur]; if(m==genA) break; if(m==genA+1){ if(haveF||path[n-1]!=cur) longjmp(JA,1); haveF=1; FA=v; break; }
    stA[cur]=genA+1; path[n++]=cur; if(n>=8192) longjmp(JA,1); v=stepval(cnt); if(v==0) longjmp(JA,1);
    memset(cnt,0,sizeof cnt); i64 w=v; for(int k=0;k<AD;k++){ cnt[w%B]++; w/=B; } cur=rank_cnt(cnt); }
  for(int i=0;i<n;i++) stA[path[i]]=genA; }
static void recA(int dg,int left,int*cnt){ if(dg==0){ cnt[0]=left; procA(cnt); return; } for(int k=0;k<=left;k++){ cnt[dg]=k; recA(dg-1,left-k,cnt); } }
static int checkA(const int*a,const int*b){ i64 p[40]; p[0]=1; for(int i=1;i<=AD;i++) p[i]=p[i-1]*B;
  i64 s=0; for(int i=0;i<AD;i++){ int aa,bb; if(i<N-1){aa=a[i];bb=b[i];} else if(i==N-1){aa=(AD>N)?N:a[N-1];bb=b[N-1];} else if(i<AD-1){aa=i+1;bb=i;} else {aa=a[N-1];bb=AD-1;} s+=p[aa]-p[bb]; CS[i]=s; }
  genA+=2; haveF=0; FA=0; if(setjmp(JA)) return 0; int cnt[B]; recA(B-1,AD,cnt); return haveF; }
static const char DG[]="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
static void prbase(i64 v){ char buf[70]; int n=0; if(v==0){ putchar('0'); return; } while(v){ buf[n++]=DG[v%B]; v/=B; } while(n--) putchar(buf[n]); }
static int A[N],Bp[N],UA[N],UB[N]; static long idx=0; static int SH,NS; static long nA=0,nB=0,ntot=0;
static void gb(int i){ if(i==N){ if(idx++%NS!=SH) return; ntot++; int f[B]; memset(f,0,sizeof f); int pa=checkA(A,Bp); i64 fa=FA; int pb=checkB(A,Bp,f);
    if(pa||pb){ nA+=pa; nB+=pb; printf("CORE N=%d a=",N); for(int k=0;k<N;k++)printf("%d%s",A[k],k<N-1?",":""); printf(" b="); for(int k=0;k<N;k++)printf("%d%s",Bp[k],k<N-1?",":"");
      printf(" A=%d B=%d endpointA=",pa,pb); prbase(pa?fa:0); printf(" target="); if(pb){ for(int g=B-1;g>=1;g--) for(int q=0;q<f[g];q++) putchar(DG[g]); printf(" maxsteps=%d maxsize=%d",maxsteps,maxsize);} else printf("-");
      printf(" base=%d\n",B); fflush(stdout);} return; }
  for(int p=0;p<N;p++){ if(UB[p]||p==A[i]) continue; UB[p]=1; Bp[i]=p; gb(i+1); UB[p]=0; } }
static void ga(int i){ if(i==N){ gb(0); return; } for(int p=0;p<N;p++){ if(UA[p]) continue; UA[p]=1; A[i]=p; ga(i+1); UA[p]=0; } }
#ifdef SINGLE
// usage: prog a0,a1,.. b0,b1,.. lo hi   -> brute-force test at every length lo..hi
int main(int argc,char**argv){ int a[N],b[N]; char*p=argv[1]; for(int i=0;i<N;i++){ a[i]=strtol(p,&p,10); p++; } p=argv[2]; for(int i=0;i<N;i++){ b[i]=strtol(p,&p,10); p++; }
  for(int n=0;n<80;n++){binom[n][0]=1; for(int k=1;k<=n;k++)binom[n][k]=binom[n-1][k-1]+(k<=n-1?binom[n-1][k]:0);}
  int lo=atoi(argv[3]),hi=atoi(argv[4]); printf("base=%d a=%s b=%s",B,argv[1],argv[2]);
  for(AD=lo;AD<=hi;AD++){ stA=calloc(binom[AD+B-1][B-1],4); genA=0; int ok=checkA(a,b); printf(" d%d:",AD); if(ok) prbase(FA); else printf("FAIL"); free(stA); }
  printf("\n"); return 0; }
#else
int main(int argc,char**argv){ SH=atoi(argv[1]); NS=atoi(argv[2]); AD=argc>3?atoi(argv[3]):N+6;
  for(int n=0;n<80;n++){binom[n][0]=1; for(int k=1;k<=n;k++)binom[n][k]=binom[n-1][k-1]+(k<=n-1?binom[n-1][k]:0);}
  stA=calloc(binom[AD+B-1][B-1],4); keys=calloc(mask+1,8); val=calloc(mask+1,2); stamp=calloc(mask+1,4); ga(0);
  printf("DONE N=%d base=%d AD=%d shard=%d cores=%ld A=%ld B=%ld\n",N,B,AD,SH,ntot,nA,nB); return 0; }
#endif
