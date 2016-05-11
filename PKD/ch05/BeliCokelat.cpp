#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ULL;

int main() {
  ULL N, D, a, b, o = 0;
  map<ULL,ULL> c;
  vector<ULL> address;
  scanf("%llu %llu",&N,&D);
  address.resize(N);
  for (ULL i = 0; i < N; i++) {
    scanf("%llu %llu",&a,&b);
    c[a] = b;
    address[i] = a;
  }
  sort(address.begin(),address.end());
  for (ULL i = 0; i < N; i++) {
    if (address[i] > D) break;
    o += min(c[address[i]], D/address[i]);
    D -= address[i] * min(c[address[i]], D/address[i]);
  }
  printf("%llu\n",o);
  return 0;
}
