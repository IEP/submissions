#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
  ll n, q, t, temp, a, b, start;
  vector<ll> d;
  cin >> n;
  for (ll i = 0; i < n; i++) {
    cin >> temp;
    d.push_back(temp);
  }
  cin >> q;
  for (ll i = 0; i < q; i++) {
    cin >> a >> b;
    t = 0;
    start = lower_bound(d.begin(), d.end(), a) - d.begin();
    for (ll j = start; j < d.size(); j++) {
      if (d[j] > a && d[j] <= b) {
        t++;
      } else if (d[j] > b) {
        break;
      }
    }
    cout << t << "\n";
  }
  return 0;
}
