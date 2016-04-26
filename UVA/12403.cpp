#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  long long m, temp;
  string c;
  cin >> t;
  m = 0;
  for (int i = 0; i < t; i++) {
    cin >> c;
    if (c == "donate") {
      cin >> temp;
      m += temp;
    } else {
      cout << m << "\n";
    }
  }
  return 0;
}
