#include <bits/stdc++.h>
using namespace std;
int main() {
  int k;
  string c, a;
  cin >> k >> c >> a;
  for (int i = 0; i < k; i++) {
    for (int j = 0; j < k; j++) {
      if (i == j | i + j == k - 1) {
        cout << a;
      } else {
        cout << c;
      }
    }
    cout << "\n";
  }
  return 0;
}
