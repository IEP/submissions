#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int M, N, p, d, x;
  vector<int> v;
  cin >> M;
  v.resize(M);
  for (int i = 0; i < M; i++)
    cin >> v[i];
  cin >> N;
  sort(v.begin(),v.end());
  p = M/N; d = M - N * p; x = 0;
  for (int i = 0; i < N-1; i++) {

  }
  return 0;
}
