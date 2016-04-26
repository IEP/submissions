#include <bits/stdc++.h>
using namespace std;

int f(int n) {
  if (n <= 100)
    return f(f(n+11));
  if (n >= 101)
    return n-10;
}

int main() {
  ios_base::sync_with_stdio(0);
  int n;
  while (1) {
    cin >> n;
    if (n == 0)
      break;
    cout << "f91(" << n << ") = " << f(n) << "\n";
  }
  return 0;
}
