#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  //cin.tie(NULL);
  int T;
  long N, H, temp, dist, pos;
  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> N >> H;
    vector<long> v;
    dist = 0;
    for (long j = 0; j < N; j++) {
      cin >> temp;
      v.push_back(temp);
    }
    sort(v.begin(),v.end());
    while (H > 0) {
      pos = upper_bound(v.begin(),v.end(),H)-v.begin();
      temp = v[pos];
      if (v[pos-1] == H) {
        temp = v[pos-1];
      } else if (temp == 0) {
        temp = v[v.size()-1];
      }
      dist += temp;
      H -= temp;
    }
    cout << dist << "\n";
  }
  return 0;
}
