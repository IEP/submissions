#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;

ll _sieve_size;
bitset<10000010> bs;
vi primes;
int factor[1000];

void sieve(ll upperbound) {
  _sieve_size = upperbound + 1;
  bs.set(); bs[0] = bs[1] = 0;
  for (ll i = 2; i <= _sieve_size; i++) if (bs[i]) {
    for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
    primes.push_back((int)i);
  }
}

int factorCount(ll n) {
  int res = 1, largest = 0;
  for (int i = 0; i < (int)primes.size(); i++) {
    if (primes[i] > n)
      break;
    while (n % primes[i] == 0) {
      factor[i]++;
      n /= primes[i];
      largest = max(largest,i);
    }
  }
  for (int i = 0; i <= largest; i++) {
    if (factor[i] > 0)
      res *= (factor[i] + 1);
  }
  return res;
}

int main() {
  sieve(1000);
  int n = 1, add = 2, res, temp;
  pair<int,int> maks;
  maks = {0,0};
  while (1) {
    memset(factor,0,sizeof factor);
    res = factorCount(n);
    if (max(res,maks.second) == res && res != temp) {
      maks = {n,res};
      temp = res;
      printf("%d %d\n",maks.first,maks.second);
    }
    if (res > 500)
      break;
    n += add;
    add++;
  }
  printf("%d\n",n);
  return 0;
}
