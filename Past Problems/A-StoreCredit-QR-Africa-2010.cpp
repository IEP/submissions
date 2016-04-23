#include <bits/stdc++.h>
using namespace std;

int main () {
  ios_base::sync_with_stdio(0);
  int N, C, I, P;
  cin >> N;
  for (int tc = 0; tc < N; tc++) {
    cin >> C >> I;
    int j, k, a, b;
    int data[I];
    for (j = 0; j < I; j++) {
      cin >> data[j];
    }
    for (j = 0; j < I; j++) {
      for (k = 0; k < j; k++) {
        if (j == k) {
          continue;
        } else if (data[j] + data[k] == C) {
          a = min(j,k)+1;
          b = max(j,k)+1;
          break;
        }
      }
    }
    printf("Case #%d: %d %d\n", tc+1, a, b);
  }
  return 0;
}
