#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

int main() {
  LL T, Z, N, C, maks;
  //freopen("63-1.in","r",stdin);
  cin >> T;
  for (LL i = 0; i < T; i++) {
    cin >> Z >> N;
    vector<LL> v;
    for (LL j = 0; j < N; j++) {
      cin >> C;
      v.push_back(C);
    }
    maks = 0;
    for (LL j = 0; j < N; j++) {
      for (LL k = 0; k < N; k++) {
        if (j == k)
          continue;
        else if (v[j] * v[k] > maks && v[j] + v[k] <= Z)
          maks = v[j] * v[k];
      }
    }
    cout << "Case #" << i+1 << ": " << maks << "\n";
  }
  return 0;
}
