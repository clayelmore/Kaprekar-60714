// Independent closure computation for the length-free map Phi on multisets of nonzero digits.
// Phi(N) := nonzero-digit multiset of K_d(N + zeros), computed from the DEFINITION of K_d with d = max(7, |N|+1),
// cross-checked against K_d at d = |N|+9 and against the V(N) formula of Lemma 3.
// Usage: ./clos max9 maxother
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef __int128 i128;
static i128 p10(int k){ i128 r=1; while(k--) r*=10; return r; }

// K_d on sorted-desc digits s[0..d-1] from the place maps
static i128 Kd(const int *s, int d){
  int a[80], b[80];
  int a0[5]={3,5,1,2,0}, b0[6]={1,4,5,3,2,0};
  for(int i=0;i<5;i++) a[i]=a0[i];
  for(int i=0;i<6;i++) b[i]=b0[i];
  if(d==6) a[5]=4; else { for(int i=5;i<=d-2;i++) a[i]=i+1; a[d-1]=4; for(int i=6;i<d;i++) b[i]=i; }
  i128 A=0,Bv=0; for(int i=0;i<d;i++){ A+=p10(a[i])*s[i]; Bv+=p10(b[i])*s[i]; }
  i128 x=A-Bv; return x<0?-x:x;
}
static i128 Vform(const int *n, int len){ // n desc, padded zeros beyond len
  int m[80]={0}; for(int i=0;i<len;i++) m[i]=n[i];
  i128 v=990*(i128)m[0]+90000*(i128)m[1]-99990*(i128)m[2]-900*(i128)m[3]-99*(i128)m[4]-(i128)m[5];
  for(int j=6;j<=len+1 && j<79;j++) v+=p10(j)*(m[j-1]-m[j]);
  return v<0?-v:v;
}
typedef uint64_t key;
static key pack(const int *c){ key k=0; for(int v=1;v<=9;v++) k|=((key)c[v])<<(6*(v-1)); return k; }
static void unpack(key k,int *c){ c[0]=0; for(int v=1;v<=9;v++) c[v]=(k>>(6*(v-1)))&63; }
static int sizeof_k(key k){ int c[10]; unpack(k,c); int s=0; for(int v=1;v<=9;v++) s+=c[v]; return s; }

static long mismatches=0;
static key phi(key k){
  int c[10]; unpack(k,c);
  int s[80]; int n=0; for(int v=9;v>=1;v--) for(int j=0;j<c[v];j++) s[n++]=v;
  int d=n+1; if(d<7) d=7;
  int t[80]; memcpy(t,s,sizeof(int)*n); for(int i=n;i<80;i++) t[i]=0;
  i128 x=Kd(t,d);
  i128 x2=Kd(t,n+9);
  i128 x3=Vform(s,n);
  if(x!=x2||x!=x3) mismatches++;
  int o[10]={0}; while(x>0){ int dg=(int)(x%10); if(dg<0||dg>9){fprintf(stderr,"neg\n");exit(1);} o[dg]++; x/=10; }
  for(int v=1;v<=9;v++) if(o[v]>63){fprintf(stderr,"pack overflow\n");exit(1);}
  return pack(o);
}
// hash table
#define HB 26
static key *HK; static int16_t *HD; static uint64_t HN=1ull<<HB, used=0;
static uint64_t hsh(key k){ k^=k>>33; k*=0xff51afd7ed558ccdULL; k^=k>>33; k*=0xc4ceb9fe1a85ec53ULL; k^=k>>33; return k&(HN-1); }
// keys stored +1 so that 0 means empty (empty multiset key=0 -> stored as 1)
static int64_t find(key k){ uint64_t h=hsh(k); while(HK[h]){ if(HK[h]==k+1) return h; h=(h+1)&(HN-1);} return -(int64_t)h-1; }
static uint64_t ins(key k,int16_t dv){ int64_t f=find(k); if(f>=0){HD[f]=dv; return f;} uint64_t h=-(f+1); HK[h]=k+1; HD[h]=dv; used++; if(used>HN*0.7){fprintf(stderr,"table full\n");exit(1);} return h; }

int main(int argc,char**argv){
  int max9=atoi(argv[1]), maxo=atoi(argv[2]);
  HK=calloc(HN,sizeof(key)); HD=malloc(HN*sizeof(int16_t));
  int tc[10]={0}; tc[1]=tc[4]=tc[6]=tc[7]=1; key T=pack(tc);
  if(phi(T)!=T){printf("target not fixed under Phi\n");}
  ins(T,0);
  int maxsize=0, maxdist=0; long seeds=0, fail=0; key argmax=0;
  key path[5000];
  int c[10];
  // enumerate seeds: c9 in 0..max9, others multiset of size <= maxo over 1..8
  for(int n9=0;n9<=max9;n9++){
    // iterate counts c1..c8 with sum<=maxo
    int cc[9]={0};
    while(1){
      int sum=0; for(int v=1;v<=8;v++) sum+=cc[v];
      if(sum<=maxo && !(sum==0&&n9==0)){
        seeds++;
        memset(c,0,sizeof c); for(int v=1;v<=8;v++) c[v]=cc[v]; c[9]=n9;
        key k=pack(c);
        int len=0; int64_t f;
        while((f=find(k))<0 || HD[f]<0){
          if(f>=0 && HD[f]==-1){ fail++; break; } // on current path: cycle
          ins(k,-1); path[len++]=k;
          int sz=sizeof_k(k); if(sz>maxsize) maxsize=sz;
          if(k==0){ fail++; break; }
          k=phi(k);
          if(len>4990){fprintf(stderr,"long path\n");exit(1);}
        }
        int base = (f>=0 && HD[f]>=0)? HD[f] : 30000;
        for(int j=len-1;j>=0;j--){ base=(base>=30000)?30000:base+1; ins(path[j],base); }
      }
      // increment
      int v=1; while(v<=8){ cc[v]++; int s2=0; for(int u=1;u<=8;u++) s2+=cc[u]; if(s2<=maxo) break; cc[v]=0; v++; }
      if(v>8) break;
    }
  }
  // scan for max dist among seeds, and over all states
  long bad=0; uint64_t states=0;
  for(uint64_t h=0;h<HN;h++) if(HK[h]){ states++; if(HD[h]>=30000) bad++; else if(HD[h]>maxdist){maxdist=HD[h]; argmax=HK[h]-1;}
    int sz=sizeof_k(HK[h]-1); if(sz>maxsize) maxsize=sz; }
  // max dist over seeds only
  int maxseed=0; key aseed=0;
  for(int n9=0;n9<=max9;n9++){ int cc[9]={0};
    while(1){ int sum=0; for(int v=1;v<=8;v++) sum+=cc[v];
      if(sum<=maxo && !(sum==0&&n9==0)){ memset(c,0,sizeof c); for(int v=1;v<=8;v++) c[v]=cc[v]; c[9]=n9; key k=pack(c); int64_t f=find(k); if(HD[f]>maxseed){maxseed=HD[f]; aseed=k;} }
      int v=1; while(v<=8){ cc[v]++; int s2=0; for(int u=1;u<=8;u++) s2+=cc[u]; if(s2<=maxo) break; cc[v]=0; v++; } if(v>8) break; } }
  printf("seeds=%ld distinct_states_visited=%llu failures(cycle or 0)=%ld bad=%ld max_nonzero_digits_visited=%d max_steps_from_seed_to_{7,6,4,1}=%d formula_mismatches=%ld\n",
    seeds,(unsigned long long)states,fail,bad,maxsize,maxseed,mismatches);
  unpack(aseed,c); printf("argmax seed counts(1..9):"); for(int v=1;v<=9;v++) printf(" %d",c[v]); printf("\n");
  (void)argmax;
}
