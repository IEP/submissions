#include <bits/stdc++.h>
using namespace std;

bitset<1000010> bs;
vector<int> prime;
long long ss;

void sieve(long long upperbound) {
  ss = upperbound + 1;
  bs.reset(); bs.flip();
  bs.set(0, false); bs.set(1, false);
  for (long long i = 2 * 1LL; i <= ss; i++)
    if (bs.test((size_t)i)) {
      for (long long j = i * 1LL * i; j <= ss; j += i)
        bs.set((size_t)j, false);
      prime.push_back((int)i);
    }
}

int main() {
  ios_base::sync_with_stdio(0);
  sieve(990100);
  int T;
  long long K;
  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> K;
    cout << prime[K-1] << "\n";
  }
  return 0;
}
