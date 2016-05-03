#include <bits/stdc++.h>
using namespace std;

int main() {
  long long N;
  vector<long long> v;
  while (cin >> N)
    v.push_back(N);
  cout << *max_element(v.begin(),v.end()) - *min_element(v.begin(),v.end()) << "\n";
  return 0;
}
