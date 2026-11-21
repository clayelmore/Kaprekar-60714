/* Independent referee check of PROOF_ALLBASE_D6.md. Written from the rule only.
   K(s) = |EABDFC - DFCEAB| with A>=B>=...>=F the sorted digits of a 6-digit base-b string.
   For each base, enumerate all digit multisets, iterate K on integers, count steps to F=(b-1)(b^3-1). */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int B;
static ll K(ll x){
  int d[6]; for(int i=0;i<6;i++){d[i]=x%B; x/=B;}
  for(int i=0;i<6;i++)for(int j=i+1;j<6;j++) if(d[j]>d[i]){int t=d[i];d[i]=d[j];d[j]=t;}
  int A=d[0],Bd=d[1],C=d[2],D=d[3],E=d[4],Fd=d[5];
  int p1[6]={E,A,Bd,D,Fd,C}, p2[6]={D,Fd,C,E,A,Bd};
  ll a=0,c=0; for(int i=0;i<6;i++){a=a*B+p1[i]; c=c*B+p2[i];}
  return a>c?a-c:c-a;
}
int main(int argc,char**argv){
  int lo=atoi(argv[1]), hi=atoi(argv[2]);
  for(B=lo;B<=hi;B++){
    ll b=B, b3=b*b*b, F=(b-1)*(b3-1);
    if(K(F)!=F){printf("b=%d F not fixed\n",B);return 1;}
    /* memo over all 6-digit values would be big; memo on images (multiples of b^3-1 below b^6) */
    ll nm=b3+1; int *memo=malloc(sizeof(int)*nm); for(ll i=0;i<nm;i++)memo[i]=-1;
    int maxs=0, fail=0; ll count=0, argmax=0;
    int s[6];
    for(s[0]=0;s[0]<B;s[0]++)for(s[1]=0;s[1]<=s[0];s[1]++)for(s[2]=0;s[2]<=s[1];s[2]++)
    for(s[3]=0;s[3]<=s[2];s[3]++)for(s[4]=0;s[4]<=s[3];s[4]++)for(s[5]=0;s[5]<=s[4];s[5]++){
      ll x=0; for(int i=0;i<6;i++) x=x*b+s[i];
      count++;
      ll y=K(x);
      if(s[0]==s[5]){ if(y!=0){printf("b=%d repdigit not ->0\n",B);fail=1;} continue; }
      if(y%(b3-1)!=0 || y/(b3-1)>=nm){printf("b=%d image not multiple\n",B);fail=1;continue;}
      /* follow orbit */
      ll path[4096]; int L=0; ll z=y; int st=-1;
      while(1){
        if(z==F){st=0;break;}
        ll mm=z/(b3-1);
        if(z%(b3-1)==0 && memo[mm]>=0){st=memo[mm];break;}
        if(L>=4000){break;}
        path[L++]=z; z=K(z);
        if(z==0){break;}
      }
      if(st<0){printf("b=%d FAIL from %lld\n",B,x);fail=1;continue;}
      for(int i=L-1;i>=0;i--){st++; memo[path[i]/(b3-1)]=st;}
      /* st now = steps from y to F */
      int tot = (x==F)?0:1+ (y==F?0:memo[y/(b3-1)]);
      if(y==F) tot = (x==F)?0:1;
      if(tot>maxs){maxs=tot;argmax=x;}
    }
    double bound=B/2.0+10;
    printf("b=%3d multisets=%9lld max_steps=%2d bound=%.1f %s%s argmax_sorted=%lld\n",B,count,maxs,bound,
      maxs<=bound?"OK":"EXCEEDS", fail?" FAIL":"", argmax);
    free(memo);
  }
  return 0;
}
