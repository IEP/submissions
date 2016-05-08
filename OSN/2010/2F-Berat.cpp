#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int w, a = 0, b = 10001;
  while (cin >> w) {
    if (w == 0) {
      cout << b << " " << a << "\n";
      a = 0;
      b = 10001;
    } else {
      a = max(a,w);
      b = min(b,w);
    }
  }
  if (a != 0 && b != 10001)
    cout << b << " " << a << "\n";
  return 0;
}
