/* Referee's independent check of the half-swap rule R_n (written from the Statement of
 * PROOF_HALFSWAP.md only).
 *
 *   ./ref_hs n b enum   : enumerate every 2n-digit multiset (all strings, since K depends only on
 *                         the multiset); report repdigits, failures, max steps to the integer F.
 *   ./ref_hs n b allm   : for EVERY m in 1..b^n-1, iterate the direct rule from K=(b^n-1)m (a superset
 *                         of all images) and report whether each reaches F or 0, and max steps.
 *
 * The rule is applied directly: word1 has s[P_q] at place q+n and s[M_q] at place q; word2 swaps;
 * K = |word1 - word2| on (128-bit) integers.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef unsigned __int128 u128;
static int n, b, P[64], M[64];
static u128 bn, Fval, bpow[130];
static uint64_t BN;            /* b^n as integer index range */
static int16_t *memo;          /* steps from m to m==b-1 ; -1 unknown, -2 in progress, -3 fails */

static void build_rule(void) {
  for (int q = 0; q < n; q++) P[q] = M[q] = -1;
  if (n % 2 == 1) {
    int k = (n - 1) / 2;
    P[0] = n; M[0] = n + 1;
    P[1] = 0; M[1] = 2 * n - 1;
    P[2] = n - 1; M[2] = n - 2;
    for (int j = 1; j <= k - 1; j++) {
      P[n + 1 - 2 * j] = 2 * j;          M[n + 1 - 2 * j] = 2 * j - 1;
      P[n - 2 * j] = 2 * n - 1 - 2 * j;  M[n - 2 * j] = 2 * n - 2 * j;
    }
  } else {
    int k = (n - 2) / 2;
    P[0] = n - 2; M[0] = n - 1;
    P[1] = 1; M[1] = 2 * n - 1;
    P[2] = 0; M[2] = 2 * n - 2;
    P[3] = n + 1; M[3] = n;
    for (int j = 1; j <= k - 1; j++) {
      P[n + 1 - 2 * j] = 2 * j + 1;      M[n + 1 - 2 * j] = 2 * j;
      P[n - 2 * j] = 2 * n - 2 - 2 * j;  M[n - 2 * j] = 2 * n - 1 - 2 * j;
    }
  }
  /* validate partition */
  int seen[128] = {0};
  for (int q = 0; q < n; q++) {
    if (P[q] < 0 || M[q] < 0 || P[q] >= 2 * n || M[q] >= 2 * n) { fprintf(stderr, "bad rule place %d\n", q); exit(2); }
    seen[P[q]]++; seen[M[q]]++;
  }
  for (int i = 0; i < 2 * n; i++) if (seen[i] != 1) { fprintf(stderr, "letter %d used %d times\n", i, seen[i]); exit(2); }
}

static u128 applyK(const int *s) {           /* s sorted descending */
  u128 w1 = 0, w2 = 0;
  for (int q = 0; q < n; q++) {
    w1 += (u128)s[P[q]] * bpow[q + n] + (u128)s[M[q]] * bpow[q];
    w2 += (u128)s[M[q]] * bpow[q + n] + (u128)s[P[q]] * bpow[q];
  }
  return w1 > w2 ? w1 - w2 : w2 - w1;
}

static u128 stepK(u128 K) {
  int cnt[1024]; memset(cnt, 0, sizeof(int) * b);
  for (int i = 0; i < 2 * n; i++) { cnt[(int)(K % b)]++; K /= b; }
  int s[128], t = 0;
  for (int d = b - 1; d >= 0; d--) for (int c = 0; c < cnt[d]; c++) s[t++] = d;
  return applyK(s);
}

static uint64_t m_of(u128 K) {
  if (K % (bn - 1) != 0) { fprintf(stderr, "K not a multiple of b^n-1\n"); exit(3); }
  return (uint64_t)(K / (bn - 1));
}

/* steps from value (b^n-1)*m to the integer F; -3 if it never reaches F */
static int steps_m(uint64_t m) {
  static uint64_t path[1 << 16];
  int len = 0;
  uint64_t x = m;
  while (1) {
    if (memo[x] >= 0 || memo[x] == -3) break;
    if (memo[x] == -2) { /* cycle not through F */
      for (int i = 0; i < len; i++) memo[path[i]] = -3;
      return -3;
    }
    memo[x] = -2; path[len++] = x;
    if (len >= (1 << 16)) { fprintf(stderr, "path overflow\n"); exit(4); }
    x = m_of(stepK((u128)x * (bn - 1)));
  }
  int base = memo[x];
  for (int i = len - 1; i >= 0; i--) {
    if (base == -3) memo[path[i]] = -3;
    else memo[path[i]] = (int16_t)(++base);
  }
  return memo[m];
}

static int s[128];
static long long nms = 0, nrep = 0, nfail = 0, nrepimg = 0;
static int maxsteps = 0;
static int hist[256];

static void leaf(void) {
  nms++;
  u128 K = applyK(s);
  int rep = (s[0] == s[2 * n - 1]);
  if (rep) { nrep++; if (K != 0) { printf("REPDIGIT NONZERO IMAGE\n"); nfail++; } return; }
  uint64_t m0 = m_of(K);
  /* is the first image itself a repdigit string? */
  { u128 t = K; int d0 = (int)(t % b), ok = 1; for (int i = 0; i < 2 * n; i++) { if ((int)(t % b) != d0) ok = 0; t /= b; } if (ok) nrepimg++; }
  int st = steps_m(m0);
  if (st < 0) {
    nfail++;
    if (nfail <= 5) { printf("FAIL multiset:"); for (int i = 0; i < 2 * n; i++) printf(" %d", s[i]); printf("\n"); }
    return;
  }
  int tot = 1 + st;      /* any arrangement other than F itself; F itself takes 0 */
  if (tot > maxsteps) maxsteps = tot;
  hist[tot]++;
}

static void rec(int i, int hi) {
  if (i == 2 * n) { leaf(); return; }
  for (int d = hi; d >= 0; d--) { s[i] = d; rec(i + 1, d); }
}

int main(int argc, char **argv) {
  if (argc < 4) { fprintf(stderr, "usage: n b enum|allm\n"); return 1; }
  n = atoi(argv[1]); b = atoi(argv[2]);
  build_rule();
  bpow[0] = 1; for (int i = 1; i < 130; i++) bpow[i] = bpow[i - 1] * (u128)b;
  bn = bpow[n]; BN = (uint64_t)bn;
  Fval = (u128)(b - 1) * (bn - 1);
  memo = malloc(sizeof(int16_t) * BN);
  for (uint64_t i = 0; i < BN; i++) memo[i] = -1;
  memo[b - 1] = 0;                    /* value F */
  /* sanity: F fixed under the direct rule */
  if (stepK(Fval) != Fval) { printf("F NOT FIXED n=%d b=%d\n", n, b); }
  if (strcmp(argv[3], "enum") == 0) {
    rec(0, b - 1);
    printf("n=%d b=%d multisets=%lld repdigits=%lld fail=%lld repdigit_first_images=%lld maxsteps=%d hist:",
           n, b, nms, nrep, nfail, nrepimg, maxsteps);
    for (int i = 0; i <= maxsteps; i++) printf(" %d", hist[i]);
    printf("\n");
  } else {
    long long fails = 0; int mx = 0; uint64_t arg = 0;
    for (uint64_t m = 1; m < BN; m++) {
      int st = steps_m(m);
      if (st < 0) { fails++; if (fails <= 3) printf("m=%llu does not reach F\n", (unsigned long long)m); }
      else if (st > mx) { mx = st; arg = m; }
    }
    printf("n=%d b=%d allm: m in 1..b^n-1, not reaching F=%lld, max steps from (b^n-1)m = %d (m=%llu)\n",
           n, b, fails, mx, (unsigned long long)arg);
  }
  return 0;
}
