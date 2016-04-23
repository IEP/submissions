#include <bits/stdc++.h>
using namespace std;
int main () {
  int i;
  cin >> i;
  for (int j = i; j > 0; j--) {
    if (i % j == 0) {
      cout << j << "\n";
    }
  }
  return 0;
}
