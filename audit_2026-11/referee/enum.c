// Referee enumerator: raw coefficients, no memo, d=6..24. Every non-repdigit multiset iterated until value 146070.
#include <stdio.h>
#include <string.h>
typedef __int128 i128;
static int d; static i128 c[40]; static unsigned long long n=0,bad=0; static int mx=0;
static void go(const int*cnt0){ int cnt[10]; memcpy(cnt,cnt0,sizeof cnt);
  for(int g=0;g<10;g++) if(cnt[g]==d) return;
  n++; for(int st=0;st<5000;st++){ i128 v=0; int i=0; for(int g=9;g>=0;g--) for(int k=0;k<cnt[g];k++) v+=c[i++]*g; if(v<0)v=-v;
    if(v==146070){ // confirm state is the fixed state
      if(cnt[7]==1&&cnt[6]==1&&cnt[4]==1&&cnt[1]==1&&cnt[0]==d-4){ if(st>mx)mx=st; return; } }
    if(v==0){bad++;return;}
    memset(cnt,0,sizeof cnt); for(int k=0;k<d;k++){cnt[(int)(v%10)]++; v/=10;} if(v!=0){bad++;return;} }
  bad++; }
static void rec(int g,int left,int*cnt){ if(g==0){cnt[0]=left; go(cnt); return;} for(int k=0;k<=left;k++){cnt[g]=k; rec(g-1,left-k,cnt);} }
int main(int argc,char**argv){ int lo=6,hi=24; if(argc>2){sscanf(argv[1],"%d",&lo);sscanf(argv[2],"%d",&hi);}
  for(d=lo;d<=hi;d++){ i128 p[40]; p[0]=1; for(int i=1;i<40&&i<=d;i++)p[i]=p[i-1]*10;
    c[0]=990;c[1]=90000;c[2]=-99990;c[3]=-900;c[4]=-99;
    if(d==6) c[5]=9999; else { c[5]=999999; for(int k=6;k<=d-2;k++) c[k]=9*p[k]; c[d-1]=-(p[d-1]-10000); }
    n=bad=0; mx=0; int cnt[10]; rec(9,d,cnt);
    printf("d=%d nonrep=%llu failures=%llu maxsteps=%d\n",d,n,bad,mx); fflush(stdout);} return 0; }
