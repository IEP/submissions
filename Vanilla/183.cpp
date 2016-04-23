#include <bits/stdc++.h>
typedef long long LL;
using namespace std;

int main() {
  LL n, d, temp;
  cin >> n >> d;
  vector<LL> arr;
  for (LL i = 0; i < n; i++) {
    cin >> temp;
    arr.push_back(temp);
  }
  sort(arr.begin(),arr.end());
  for (LL i = 0; i < arr.size(); i++) {
    if (arr[i] == d) {
      cout << i << "\n";
      break;
    } else if (arr[i] > d) {
      cout << -1 << "\n";
      break;
    }
  }
  return 0;
}
