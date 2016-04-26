#include <bits/stdc++.h>
using namespace std;

vector<long long> v;

long long median() {
  long long n = v.size();
  if (n % 2 == 0)
    return (v[n/2] + v[n/2+1])/2;
  return v[(n+1)/2];
}

int main() {
  ios_base::sync_with_stdio(0);
  long long i;
  while (cin >> i) {
    v.push_back(i);
    sort(v.begin(),v.end());
    cout << median() << "\n";
  }
  return 0;
}
