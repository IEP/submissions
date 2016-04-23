#include <bits/stdc++.h>
using namespace std;
int main () {
  double i, k;
  int j;
  cin >> i;
  j = (int)(log(i)/log(2));
  k = pow(2,j);
  if (i == k) {
    cout << "ya\n";
  } else {
    cout << "bukan\n";
  }
  //cout << j << " " << k << "\n";
  return 0;
}
