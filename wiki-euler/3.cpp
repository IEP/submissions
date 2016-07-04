#include <bits/stdc++.h>
using namespace std;

long long _sieve_size;
bitset<10000010> bs;

void sieve(long long upperbound) {
  _sieve_size = upperbound + 1;
  bs.set();
  bs[0] = bs[1] = 0;
  for (long long i = 2; i <= _sieve_size; i++) if (bs[i]) {
    for (long long j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  sieve(800000);
  for (int i = ceil(sqrt(600851475143)); i > 0; i--) {
    if (bs[i] && 600851475143 % i == 0) {
      cout << i << "\n";
      break;
    }
  }
  return 0;
}
