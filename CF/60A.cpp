#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, m;
  string h, t;
  cin >> n >> m;
  int a = 0, b = n, c;
  for (int i = 0; i < m; i++) {
    cin >> t >> t >> h >> t >> c;
    if (h == "left")
      b = min(b,c-1);
    else
      a = max(a,c);
  }
  if (b - a > 0)
    cout << b - a << "\n";
  else
    cout << "-1\n";
  return 0;
}
