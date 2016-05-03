#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int frek[100001], N;
  long long D;
  memset(frek,0,sizeof frek);
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> D;
    for (int j = D; j < 100001; j += D) {
      frek[j]++;
    }
  }
  for (long long i = 0; i < 100001; i++) {
    if (frek[i] == N) {
      cout << i << "\n";
      break;
    }
  }
  return 0;
}
