#include <bits/stdc++.h>
using namespace std;
typedef long L;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  L T, N, maks, temp;
  cin >> T;
  for (L i = 0; i < T; i++) {
    maks = 0;
    cin >> N;
    for (L j = 0; j < N; j++) {
      cin >> temp;
      temp += j;
      if (temp > maks) {
        maks = temp;
      }
    }
    cout << maks << "\n";
  }
  return 0;
}
