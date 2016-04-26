#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int N;
  vector<int> H;
  long long B, temp;
  vector<long long> p;
  cin >> N >> B;
  H.resize(N);
  p.resize(N);
  for (int i = 0; i < N; i++)
    cin >> H[i];
  sort(H.begin(),H.end());
  temp = 0;
  for (int i = 0; i < N; i++) {
    temp += H[i];
    p[i] = temp;
  }
  cout << N - (upper_bound(p.begin(),p.end(),B) - p.begin()) << "\n";
  return 0;
}
