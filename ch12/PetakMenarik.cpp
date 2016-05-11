#include <bits/stdc++.h>
using namespace std;

int N, M, K;
int d[110][110];

inline int gv(int r, int c) {
  if (r == -1 || r == N || c == -1 || c == M)
    return 1;
  return d[r][c];
}

int main() {
  ios_base::sync_with_stdio(0);
  memset(d,0,sizeof d);
  bool flag = 0;
  cin >> N >> M >> K;
  for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++)
      cin >> d[i][j];
  pair<int,int> res = {0,0};
  for (int j = 0; j < M; j++) {
    if (flag) break;
    for (int i = 0; i < N; i++)
      if (K == gv(i-1,j) * gv(i,j+1) * gv(i+1,j) * gv(i,j-1)) {
        res = {i+1,j+1};
        flag = 1;
        break;
      }
  }
  cout << res.first << " " << res.second << "\n";
  return 0;
}
