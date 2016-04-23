#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  bitset<6> flag;
  flag.set();
  int N, M, temp;
  cin >> N >> temp;
  int A[N][N];
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      cin >> A[i][j];
  cin >> M >> temp;
  if (N != M) {
    cout << "tidak identik";
  } else {
    for (int i = 0; i < M; i++)
      for (int j = 0; j < M; j++) {
        cin >> temp;
        if (A[i][j] != temp)
          if (flag.test((size_t)0))
            flag.set((size_t)0,0);
        if (A[i][M-j-1] != temp)
          if (flag.test((size_t)1))
            flag.set((size_t)1,0);
        if (A[M-i-1][j] != temp)
          if (flag.test((size_t)2))
            flag.set((size_t)2,0);
        if (A[j][i] != temp)
          if (flag.test((size_t)3))
            flag.set((size_t)3,0);
        if (A[M-j-1][M-i-1] != temp)
          if (flag.test((size_t)4))
            flag.set((size_t)4,0);
      }
    string res[] = {"identik", "vertikal", "horisontal",
                    "diagonal kanan bawah",
                    "diagonal kiri bawah",
                    "tidak identik"};
    for (size_t i = 0; i < 6; i++)
      if (flag.test(i)) {
        cout << res[i] << "\n";
        break;
      }
  }
  return 0;
}
