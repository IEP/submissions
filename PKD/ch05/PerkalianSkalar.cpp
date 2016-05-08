#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  long long N, temp, total;
  cin >> N;
  vector<long long> v1, v2;
  for (long long i = 0; i < N; i++) {
    cin >> temp;
    v1.push_back(temp);
  }
  sort(v1.begin(), v1.end());
  for (long long i = 0; i < N; i++) {
    cin >> temp;
    v2.push_back(temp);
  }
  sort(v2.begin(), v2.end());
  reverse(v2.begin(), v2.end());
  total = 0;
  for (long long i = 0; i < N; i++) {
    total += (v1[i] * v2[i]);
  }
  cout << total << "\n";
  return 0;
}
