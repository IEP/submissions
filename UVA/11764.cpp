#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  int T, step, high, low;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cin >> step;
    int stepMap[step];
    high = 0;
    low = 0;
    for (int j = 0; j < step; j++) {
      cin >> stepMap[j];
    }
    for (int j = 0; j < step-1; j++) {
      if (stepMap[j] < stepMap[j+1])
        high++;
      else if (stepMap[j] > stepMap[j+1])
        low++;
    }
    cout << "Case " << i << ": " << high << " " << low << "\n";
  }
  return 0;
}
