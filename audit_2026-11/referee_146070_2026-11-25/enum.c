// Independent complete enumeration of the 146070 rule at lengths d.
// Usage: ./enum dmin dmax
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef __int128 i128;
static uint64_t B[64][64];
static int D;
static i128 C[64];
static int32_t *mapv; static int16_t *dist; static uint8_t *is146; static int16_t *fi;
static uint64_t N;
static int maxR = 0; static uint64_t nfix = 0;

static i128 p10(int k){ i128 r=1; while(k--) r*=10; return r; }

static void coeffs(int d){
  // place maps: a=(3,5,1,2,0,6,...,d-1,4) b=(1,4,5,3,2,0,6,...,d-1); d=6: a=(3,5,1,2,0,4) b=(1,4,5,3,2,0)
  int a[64], b[64];
  int a0[5]={3,5,1,2,0}, b0[6]={1,4,5,3,2,0};
  for(int i=0;i<5;i++) a[i]=a0[i];
  for(int i=0;i<6;i++) b[i]=b0[i];
  if(d==6){ a[5]=4; }
  else { for(int i=5;i<=d-2;i++) a[i]=i+1; a[d-1]=4; for(int i=6;i<d;i++) b[i]=i; }
  // sanity: permutations
  int ua[64]={0},ub[64]={0};
  for(int i=0;i<d;i++){ ua[a[i]]++; ub[b[i]]++; }
  for(int i=0;i<d;i++) if(ua[i]!=1||ub[i]!=1){fprintf(stderr,"bad perm\n");exit(1);}
  for(int i=0;i<d;i++) C[i]=p10(a[i])-p10(b[i]);
}

static uint64_t rank_counts(const int *cnt){ // colex rank of multiset of size D
  uint64_t r=0; int i=0;
  for(int v=0;v<10;v++) for(int k=0;k<cnt[v];k++){ r+=B[v+i][i+1]; i++; }
  return r;
}

static void image_counts(const int *cnt, int *out, i128 *val){
  int s[64]; int n=0;
  for(int v=9;v>=0;v--) for(int k=0;k<cnt[v];k++) s[n++]=v;
  i128 x=0; for(int i=0;i<D;i++) x+=C[i]*s[i];
  if(x<0) x=-x;
  *val=x;
  memset(out,0,10*sizeof(int));
  i128 y=x; int nd=0;
  while(y>0){ out[(int)(y%10)]++; y/=10; nd++; }
  if(nd>D){fprintf(stderr,"overflow digits\n");exit(1);}
  out[0]+=D-nd;
}

static int cur[10];
static void gen(int v, int left){
  if(v==9){ cur[9]=left;
    uint64_t r=rank_counts(cur); int out[10]; i128 val;
    image_counts(cur,out,&val);
    uint64_t ri=rank_counts(out);
    mapv[r]=(int32_t)ri; is146[r]=(val==146070);
    if(ri==r) nfix++;
    // non-9 nonzero digits of image (Lemma 1's R) for non-repdigit inputs
    int rep=0; for(int k=0;k<10;k++) if(cur[k]==D) rep=1;
    if(!rep){ int R=0; for(int k=1;k<=8;k++) R+=out[k]; if(R>maxR) maxR=R; }
    return; }
  for(int c=0;c<=left;c++){ cur[v]=c; gen(v+1,left-c); }
}

int main(int argc,char**argv){
  for(int n=0;n<64;n++){ B[n][0]=1; for(int k=1;k<=n;k++) B[n][k]=B[n-1][k-1]+(k<=n-1?B[n-1][k]:0); }
  int dmin=atoi(argv[1]), dmax=atoi(argv[2]);
  for(D=dmin; D<=dmax; D++){
    coeffs(D);
    N=B[D+9][9];
    mapv=malloc(N*sizeof(int32_t)); dist=malloc(N*sizeof(int16_t)); is146=malloc(N); fi=malloc(N*sizeof(int16_t));
    maxR=0; nfix=0;
    gen(0,D);
    // target
    int tc[10]={0}; tc[1]=1;tc[4]=1;tc[6]=1;tc[7]=1;tc[0]=D-4;
    uint64_t T=rank_counts(tc);
    // verify the integer: K(146070-digits)=146070
    int o[10]; i128 v; image_counts(tc,o,&v);
    int fixok = (v==146070);
    // repdigit ranks
    for(uint64_t i=0;i<N;i++) dist[i]=-1;
    dist[T]=0;
    // note: dist counts steps until the multiset equals that of 146070.
    // Steps to the integer: an input whose multiset is {1,4,6,7,0..} is the integer only if it is 146070 itself;
    // any other arrangement needs one more step. We report both.
    int16_t *onstack=calloc(N,sizeof(int16_t));
    uint64_t nrep=0, fails=0; int maxd=0; uint64_t argmax=0;
    uint64_t *path=malloc(4096*sizeof(uint64_t));
    for(uint64_t i=0;i<N;i++){
      if(dist[i]>=0) continue;
      int len=0; uint64_t x=i;
      while(dist[x]<0){
        if(onstack[x]){ fails++; break; }
        onstack[x]=1; path[len++]=x; x=mapv[x];
        if(len>4000){fprintf(stderr,"long\n");exit(1);}
      }
      int base = dist[x]>=0? dist[x] : 30000; // 30000 = failure marker
      for(int k=len-1;k>=0;k--){ base = (base>=30000)?30000:base+1; dist[path[k]]=base; onstack[path[k]]=0; }
    }
    // repdigits: count failing nonrep
    uint64_t nonrep=0;
    for(int r=0;r<10;r++){ int cc[10]={0}; cc[r]=D; uint64_t rr=rank_counts(cc); dist[rr]=-2; nrep++; }
    for(uint64_t i=0;i<N;i++){ if(dist[i]==-2) continue; nonrep++;
      if(dist[i]>=30000) fails++; else if(dist[i]>maxd){maxd=dist[i];argmax=i;} }
    // the fail count above may double count the cycle break; recount purely
    uint64_t bad=0; for(uint64_t i=0;i<N;i++) if(dist[i]>=30000) bad++;
    // the repdigits: confirm they map to 0^D (rank 0)
    int repok=1; for(int r=0;r<10;r++){ int cc[10]={0}; cc[r]=D; if(mapv[rank_counts(cc)]!=0) repok=0; }
    // f(M) = steps for a worst-case arrangement of M (M != target) ... integer x with multiset M, x != 146070:
    // steps(x) = 1 + (K(M)==146070 ? 0 : steps(K(M)))
    int maxi=0;
    for(uint64_t i=0;i<N;i++) fi[i]=-1;
    for(uint64_t i=0;i<N;i++){
      if(dist[i]==-2 || dist[i]>=30000 || fi[i]>=0) continue;
      int len=0; uint64_t x=i;
      while(fi[x]<0){ path[len++]=x; if(is146[x]) break; x=mapv[x]; }
      int base;
      if(fi[x]>=0 && !(len>0 && path[len-1]==x)) base=fi[x];
      else { base=1; fi[path[len-1]]=1; len--; }
      for(int k=len-1;k>=0;k--){ base=base+1; fi[path[k]]=base; }
    }
    for(uint64_t i=0;i<N;i++) if(fi[i]>maxi) maxi=fi[i];
    printf("  max steps to the integer 146070 (worst arrangement, inputs other than 146070 itself) = %d ; bound floor((d-1)/5)+43 = %d\n", maxi, (D-1)/5+43);
    printf("d=%d multisets=%llu nonrep=%llu bad=%llu fixedpoints(multiset-level)=%llu K(target)=146070:%d repdigits->0:%d maxSteps_to_target_multiset=%d maxR=%d\n",
      D,(unsigned long long)N,(unsigned long long)nonrep,(unsigned long long)bad,(unsigned long long)nfix,fixok,repok,maxd,maxR);
    // print argmax multiset
    { uint64_t r=argmax; int y[64]; int k=D; // unrank colex
      for(int i=D;i>=1;i--){ int c=i-1; while(B[c+1][i]<=r) c++; y[i-1]=c; r-=B[c][i]; }
      printf("  argmax multiset (ascending): "); for(int i=0;i<D;i++) printf("%d",y[i]-i); printf("\n"); (void)k; }
    fflush(stdout);
    free(mapv); free(dist); free(is146); free(fi); free(onstack); free(path);
  }
}
