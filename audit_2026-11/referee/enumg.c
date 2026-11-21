// Referee general enumerator from the raw permutation definition. usage: enumg d a0..a5 b0..b5
// Every non-repdigit multiset is iterated (no memo) until its image equals itself; reports distinct fixed values and non-converging count.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef __int128 i128;
static int d; static i128 c[40]; static unsigned long long n=0,bad=0; static int mx=0; static i128 fixv[16]; static unsigned long long fixn[16]; static int nf=0;
static void go(const int*cnt0){ int cnt[10],nx[10]; memcpy(cnt,cnt0,sizeof cnt);
  for(int g=0;g<10;g++) if(cnt[g]==d) return;
  n++; for(int st=0;st<3000;st++){ i128 v=0; int i=0; for(int g=9;g>=0;g--) for(int k=0;k<cnt[g];k++) v+=c[i++]*g; if(v<0)v=-v; i128 v0=v;
    memset(nx,0,sizeof nx); for(int k=0;k<d;k++){nx[(int)(v%10)]++; v/=10;} if(v!=0){bad++;return;}
    if(!memcmp(nx,cnt,sizeof nx)){ if(st>mx)mx=st; int j; for(j=0;j<nf;j++) if(fixv[j]==v0) break; if(j==nf){ if(nf<16){fixv[nf]=v0;fixn[nf]=0;nf++;} else {bad++;return;} } fixn[j]++; return; }
    memcpy(cnt,nx,sizeof cnt); }
  bad++; }
static void rec(int g,int left,int*cnt){ if(g==0){cnt[0]=left; go(cnt); return;} for(int k=0;k<=left;k++){cnt[g]=k; rec(g-1,left-k,cnt);} }
int main(int argc,char**argv){ d=atoi(argv[1]); int a6[6],b6[6]; for(int i=0;i<6;i++){a6[i]=atoi(argv[2+i]); b6[i]=atoi(argv[8+i]);}
  int a[40],b[40]; for(int i=0;i<5;i++){a[i]=a6[i]; b[i]=b6[i];} for(int i=5;i<=d-2;i++) a[i]=i+1; a[d-1]=a6[5]; b[5]=b6[5]; for(int i=6;i<=d-1;i++) b[i]=i;
  i128 p[40]; p[0]=1; for(int i=1;i<40;i++)p[i]=p[i-1]*10; i128 s=0; for(int i=0;i<d;i++){c[i]=p[a[i]]-p[b[i]]; s+=c[i];} if(s!=0){printf("bad coefs\n");return 1;}
  int cnt[10]; rec(9,d,cnt);
  printf("d=%d a=%d%d%d%d%d%d b=%d%d%d%d%d%d nonrep=%llu nonconverging=%llu maxsteps=%d fixed:",d,a6[0],a6[1],a6[2],a6[3],a6[4],a6[5],b6[0],b6[1],b6[2],b6[3],b6[4],b6[5],n,bad,mx);
  for(int j=0;j<nf;j++){ printf(" %lld(x%llu)",(long long)fixv[j],fixn[j]); } printf("\n"); return 0; }
