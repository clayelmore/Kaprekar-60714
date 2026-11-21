/* phi_check.c -- finite check of the length-free map Phi for one core.
 *
 * Usage: phi_check a0 a1 a2 a3 a4 a5 b0 b1 b2 b3 b4 b5 TARGET [max9 max18]
 *   TARGET = nonzero digits of the target multiset, e.g. 7641.
 * Seeds S = all nonempty multisets of nonzero digits with <= max9 nines (default 5)
 *   and <= max18 digits from 1..8 (default 15).
 * Follows Phi from every seed with memoization. Prints one summary line plus
 * examples of failing seeds.
 *
 * Multiset = counts c[1..9], packed 6 bits per digit into a uint64 key.
 * V uses __int128 (|V| < 10^38 is ample for sizes up to ~30).
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef __int128 i128;
static int A[6], B[6];
static i128 P10[40];

#define HBITS 24
#define HSIZE (1u << HBITS)
static uint64_t *hkey;   /* 0 = empty slot; keys stored +1 offset not needed since empty multiset key 0 handled separately */
static int32_t *hval;    /* >=0 distance to target; -1 = on current path; -2 = fails (empty or cycle) */
static long nstates = 0;

#define EMPTY_SLOT UINT64_MAX

static uint64_t hashk(uint64_t k) { k ^= k >> 33; k *= 0xff51afd7ed558ccdULL; k ^= k >> 33; k *= 0xc4ceb9fe1a85ec53ULL; k ^= k >> 33; return k; }

static int32_t *lookup(uint64_t key, int create) {
    uint64_t h = hashk(key) & (HSIZE - 1);
    while (hkey[h] != EMPTY_SLOT) {
        if (hkey[h] == key) return &hval[h];
        h = (h + 1) & (HSIZE - 1);
    }
    if (!create) return NULL;
    if (++nstates > (long)(HSIZE * 0.7)) { fprintf(stderr, "hash table full\n"); exit(2); }
    hkey[h] = key; hval[h] = -3; /* -3 = fresh/unknown */
    return &hval[h];
}

static int keysize(uint64_t key) { int s = 0; for (int d = 1; d <= 9; d++) s += (key >> (6 * (d - 1))) & 63; return s; }

static uint64_t phi(uint64_t key) {
    int n[80]; int k = 0;
    for (int d = 9; d >= 1; d--) { int c = (key >> (6 * (d - 1))) & 63; while (c--) n[k++] = d; }
    for (int i = k; i < k + 8; i++) n[i] = 0;
    if (k + 1 >= 38) { fprintf(stderr, "multiset too large (%d)\n", k); exit(3); }
    i128 V = 0;
    for (int i = 0; i < 5; i++) V += (P10[A[i]] - P10[B[i]]) * n[i];
    V -= P10[B[5]] * n[5];
    for (int j = 6; j <= k; j++) V += P10[j] * (n[j - 1] - n[j]);
    if (V < 0) V = -V;
    uint64_t out = 0;
    while (V > 0) {
        int dg = (int)(V % 10); V /= 10;
        if (dg) {
            int c = (out >> (6 * (dg - 1))) & 63;
            if (c >= 63) { fprintf(stderr, "count overflow\n"); exit(4); }
            out += (uint64_t)1 << (6 * (dg - 1));
        }
    }
    return out;
}

static void keystr(uint64_t key, char *buf) {
    int p = 0;
    for (int d = 9; d >= 1; d--) { int c = (key >> (6 * (d - 1))) & 63; while (c--) buf[p++] = '0' + d; }
    if (p == 0) { strcpy(buf, "{}"); return; }
    buf[p] = 0;
}

int main(int argc, char **argv) {
    if (argc < 14) { fprintf(stderr, "usage\n"); return 1; }
    for (int i = 0; i < 6; i++) { A[i] = atoi(argv[1 + i]); B[i] = atoi(argv[7 + i]); }
    const char *tstr = argv[13];
    int max9 = argc > 14 ? atoi(argv[14]) : 5;
    int max18 = argc > 15 ? atoi(argv[15]) : 15;
    P10[0] = 1; for (int i = 1; i < 40; i++) P10[i] = P10[i - 1] * 10;

    hkey = malloc(sizeof(uint64_t) * HSIZE); hval = malloc(sizeof(int32_t) * HSIZE);
    for (uint64_t i = 0; i < HSIZE; i++) hkey[i] = EMPTY_SLOT;

    uint64_t target = 0;
    for (const char *p = tstr; *p; p++) { int d = *p - '0'; if (d < 1 || d > 9) { fprintf(stderr, "bad target\n"); return 1; } target += (uint64_t)1 << (6 * (d - 1)); }
    uint64_t ptarget = phi(target);
    char buf[128], buf2[128];
    *lookup(target, 1) = 0;
    *lookup(0, 1) = -2; /* empty multiset: Phi(empty) = empty, never reaches target */

    long nseeds = 0, nfail = 0, nfail_empty = 0, nfail_cycle = 0;
    int maxsteps = 0, maxsize = 0, maxsize_image = 0;
    char maxsteps_seed[128] = "", maxsize_img_ex[128] = "";
    int nex = 0;

    static uint64_t path[100000];
    int c[10];
    /* enumerate counts c1..c8 with sum <= max18, c9 <= max9 */
    memset(c, 0, sizeof c);
    for (;;) {
        int s18 = 0; for (int d = 1; d <= 8; d++) s18 += c[d];
        if (s18 <= max18) {
            for (int c9 = 0; c9 <= max9; c9++) {
                if (s18 == 0 && c9 == 0) continue;
                uint64_t key = 0;
                for (int d = 1; d <= 8; d++) key |= (uint64_t)c[d] << (6 * (d - 1));
                key |= (uint64_t)c9 << 48;
                nseeds++;
                int sz = s18 + c9; if (sz > maxsize) maxsize = sz;
                /* follow */
                int plen = 0; uint64_t cur = key; int32_t *v = lookup(cur, 1);
                int result; int is_cycle = 0, is_empty = 0;
                while (*v == -3) {
                    *v = -1; path[plen++] = cur;
                    if (plen >= 100000) { fprintf(stderr, "path too long\n"); return 5; }
                    cur = phi(cur);
                    int csz = keysize(cur);
                    if (csz > maxsize_image) { maxsize_image = csz; keystr(cur, maxsize_img_ex); }
                    if (csz > maxsize) maxsize = csz;
                    v = lookup(cur, 1);
                }
                if (*v == -1) {
                    result = -2; is_cycle = 1;
                    static int ncyc = 0;
                    if (ncyc++ < 10) {
                        printf("CYCLE:"); uint64_t x = cur; int len = 0;
                        do { keystr(x, buf); printf(" %s", buf); x = phi(x); len++; } while (x != cur && len < 1000);
                        printf("  (period %d)\n", len);
                    }
                }
                else if (*v == -2) { result = -2; if (cur == 0) is_empty = 1; else is_cycle = 2; }
                else result = *v;
                for (int i = plen - 1; i >= 0; i--) {
                    int32_t *pv = lookup(path[i], 0);
                    if (result >= 0) { result++; *pv = result; } else *pv = -2;
                }
                v = lookup(key, 0);
                if (*v >= 0) {
                    if (*v > maxsteps) { maxsteps = *v; keystr(key, maxsteps_seed); }
                } else {
                    nfail++;
                    if (is_empty) nfail_empty++; else nfail_cycle++;
                    if (nex < 10) {
                        keystr(key, buf); keystr(cur, buf2);
                        printf("FAIL seed=%s ends_at=%s (%s)\n", buf, buf2,
                               is_empty ? "empty" : (is_cycle == 1 ? "new cycle" : "known failing state"));
                        nex++;
                    }
                }
            }
        }
        /* next c1..c8 (odometer, each 0..max18) */
        int d = 1;
        while (d <= 8) { if (++c[d] <= max18) break; c[d] = 0; d++; }
        if (d > 8) break;
    }
    keystr(ptarget, buf);
    printf("core a=%d,%d,%d,%d,%d,%d b=%d,%d,%d,%d,%d,%d target=%s phi(target)=%s fixed=%d\n",
           A[0], A[1], A[2], A[3], A[4], A[5], B[0], B[1], B[2], B[3], B[4], B[5], tstr, buf, ptarget == target);
    printf("RESULT seeds=%ld fail=%ld fail_empty=%ld fail_cycle=%ld states=%ld maxsteps=%d maxsteps_seed=%s maxsize=%d maxsize_nonseed=%d maxsize_nonseed_example=%s\n",
           nseeds, nfail, nfail_empty, nfail_cycle, nstates, maxsteps, maxsteps_seed, maxsize, maxsize_image, maxsize_img_ex);
    return 0;
}
