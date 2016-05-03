#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int matrix[200][200], B, K, M, N;
  long long partial, global_max;
  bool gm = 0;
  cin >> M >> N >> B >> K;
  for (int i = 0; i < M; i++)
    for (int j = 0; j < N; j++)
      cin >> matrix[i][j];
  for (int i = 0; i < M; i++)
    for (int j = N; j < 2*N; j++)
      matrix[i][j] = matrix[i][j-N];
  for (int i = 0; i < M; i++)
    for (int j = 0; j < N; j++) {
      partial = 0;
      for (int x = i; x < i + B; x++)
        for (int y = j; y < j + K; y++)
          partial += matrix[x][y];
      if (!gm) {
        global_max = partial;
        gm = 1;
      }
      global_max = max(global_max,partial);
    }
  cout << global_max << "\n";
  return 0;
}
