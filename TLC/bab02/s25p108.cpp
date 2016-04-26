#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int A, B, C, D, temp;
  cin >> A >> B;
  int X[A][B];
  for (int i = 0; i < A; i++)
    for (int j = 0; j < B; j++)
      cin >> X[i][j];
  cin >> C >> D;
  int Y[C][D];
  for (int i = 0; i < C; i++)
    for (int j = 0; j < D; j++)
      cin >> Y[i][j];
  int Z[A][D];
  for (int i = 0; i < A; i++) {
    for (int j = 0; j < D; j++) {
      temp = 0;
      for (int k = 0; k < B; k++) {
        temp += X[i][k] * Y[k][j];
      }
      Z[i][j] = temp;
    }
  }
  for (int i = 0; i < A; i++) {
    for (int j = 0; j < D; j++) {
      cout << Z[i][j];
      if (j < D - 1)
        cout << " ";
      else
        cout << "\n";
    }
  }
  return 0;
}
