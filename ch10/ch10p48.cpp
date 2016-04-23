#include <bits/stdc++.h>
using namespace std;

vector<long long> q = vector<long long>();

bool prime(long long x) {
  long long lim = sqrt(x)+1;
  if (x < 2) {
    return 0;
  }
  for (long long i = 2; i < lim; i++) {
    if (x % i == 0) {
      return 1;
    }
  }
  return 1;
}

int hitung(long long x) {
  int t = 0;
  for (auto &i : q) {
    if (i == x) {
      t++;
    }
  }
  return t;
}

int main() {
  long long n, a, last;
  cin >> n;
  a = 2;
  last = 0;
  while (n >= a) {
    if (prime(a) && n % a == 0) {
      n /= a;
      q.push_back(a);
    } else {
      a++;
    }
  }
  for (auto &i : q) {
    if (i == last) {
      continue;
    } else {
      if (hitung(i) > 1) {
        cout << i << "^" << hitung(i);
      } else if (hitung(i) == 1) {
        cout << i;
      }
      last = i;
      if (i < q[q.size()-1]) {
        cout << " x ";
      }
    }
  }
  cout << "\n";
  return 0;
}
