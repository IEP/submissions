#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  long n, h, temp, dist, pos;
  dist = 0;
  vector<long> v;
  cin >> n >> h;
  for (long i = 0; i < n; i++) {
    cin >> temp;
    v.push_back(temp);
  }
  sort(v.begin(),v.end());
  while (h > 0) {
    pos = upper_bound(v.begin(),v.end(),h)-v.begin();
    temp = v[pos];
    if (v[pos-1] == h) {
      temp = v[pos-1];
    } else if (temp == 0) {
      temp = v[v.size()-1];
    }
    dist += temp;
    h -= temp;
  }
  cout << dist << "\n";
  return 0;
}
