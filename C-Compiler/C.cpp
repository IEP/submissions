#include <bits/stdc++.h>
using namespace std;

int main() {
  http://127.0.0.1/titip-absen/
  ios_base::sync_with_stdio(0);
  int n, temp;
  cin >> n;
  long long res = 0;
  for (int i = 0; i < n; i++) {
    cin >> temp;
    res = max(res * temp, res + temp);
  }
  cout << res << "\n";
  return 0;
}
