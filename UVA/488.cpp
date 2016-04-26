#include <bits/stdc++.h>
using namespace std;

void wave(int amp) {
  for (int i = 1; i <= amp; i++) {
    for (int j = 1; j <= i; j++) {
      cout << i;
    }
    cout << "\n";
  }
  for (int i = amp-1; i >= 1; i--) {
    for (int j = 1; j <= i; j++) {
      cout << i;
    }
    cout << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  int T, a, f;
  cin >> T;
  while (T--) {
    cin >> a >> f;
    for (int i = 0; i < f; i++)
      wave(a);
    cout << "\n";
  }
  return 0;
}
