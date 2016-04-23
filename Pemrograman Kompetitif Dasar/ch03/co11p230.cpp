#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int T, L;
  cin >> T;
  while (T--) {
    cin >> L;
    int a[L], res[L][L];
    for (int i = 0; i < L; i++) cin >> a[i];
    vector<int> v (a, a+L);
    sort(v.begin(), v.end());
    for (int i = 0; i < L; i++)
      for (int j = 0; j < L; j++)
        if (i == j)
          continue;
        else
          res[i][j] = 3;
  }
  return 0;
}
