#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int W, H, n, a, b, c, d, K;
  cin >> W >> H >> n;
  int canvas[H][W];
  memset(canvas, 0, sizeof canvas);
  for (int i = 0; i < n; i++) {
    cin >> a >> b >> c >> d >> K;
    for (int j = a-1; j < c; j++)
      for (int k = b-1; k < d; k++)
        canvas[k][j] = K;
  }
  for (int i = 0; i < H; i++)
    for (int j = 0; j < W; j++) {
      cout << canvas[i][j];
      if (j == W - 1) cout << "\n";
    }
  return 0;
}
