#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  long N, Q;
  long long temp;
  vector<long long> animal;
  cin >> N;
  animal.resize(N);
  for (long i = 0; i < N; i++) {
    if (i == 0)
      cin >> animal[0];
    else {
      cin >> temp;
      animal[i] = animal[i-1] + temp;
    }
  }
  cin >> Q;
  for (long i = 0; i < Q; i++) {
    cin >> temp;
    cout << lower_bound(animal.begin(),animal.end(),temp) - animal.begin() + 1;
    cout << "\n";
  }
  return 0;
}
