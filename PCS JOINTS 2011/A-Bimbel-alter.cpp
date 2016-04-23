#include <bits/stdc++.h>
using namespace std;

int main () {
  int N, M, res;
  cin >> N >> M;
  N++;
  res = (N % M != 0) ? 0 : 1;
  cout << N - (int)(N/M) + res << "\n";
  return 0;
}
