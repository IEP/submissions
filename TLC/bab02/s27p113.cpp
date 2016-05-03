#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

LL __sieve_size;
bitset<1000000> bs;

void sieve(LL upperbound) {
  __sieve_size = upperbound + 1;
  bs.reset(); bs.flip();
  bs.set(0,false); bs.set(1,false);
  for (LL i = 2; i <= __sieve_size; i++)
    if (bs.test((size_t)i))
      for (LL j = i * i; j <= __sieve_size; j += i)
        bs.set((size_t)j,false);
}

int main() {
  ios_base::sync_with_stdio(0);
  sieve(33000);
  int N;
  while (cin >> N) {
    if (N < 0) {
      cout << "TIDAK\n";
    } else {
      if (bs.test((size_t)N))
        cout << "YA\n";
      else
        cout << "TIDAK\n";
    }
  }
  return 0;
}
