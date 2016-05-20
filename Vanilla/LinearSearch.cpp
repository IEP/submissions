#include <bits/stdc++.h>
using namespace std;

int main() {
  bool flag = 0;
  long long n, d;
  vector<long long> v;
  scanf("%lld %lld",&n,&d);
  v.resize(n);
  for (long long i = 0; i < n; i++) {
    scanf("%lld",&v[i]);
    if (v[i] == d)
      flag = 1;
  }
  sort(v.begin(),v.end());
  if (flag)
    cout << lower_bound(v.begin(),v.end(),d) - v.begin() << "\n";
  else
    cout << "-1\n";
  return 0;
}
