#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int N, K, temp, result;
  result = 1000000000 * 1LL;
  vector<int> number;
  cin >> N >> K;
  for (int i = 0; i < N; i++) {
    cin >> temp;
    number.push_back(temp);
  }
  sort(number.begin(), number.end());
  for (int i = 0; i < N-K+1; i++) {
    result = min(result,abs(number[i]-number[i+K-1]));
  }
  cout << result << "\n";
  return 0;
}
