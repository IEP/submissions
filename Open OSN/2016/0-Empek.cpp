#include <bits/stdc++.h>
using namespace std;

int res, n;
char d[100001];
map<char,vector<int>> memo;

int main() {
  ios_base::sync_with_stdio(0);
  string temp;
  int a, b;
  cin >> temp >> n >> d;
  res = 0;
  for (int i = 0; i < n; i++)
    memo[d[i]].push_back(i);
  for (int i = 0; i < memo['1'].size(); i++) {
    a = upper_bound(memo['2'].begin(),memo['2'].end(),memo['1'][i])-memo['2'].begin();
    for (int j = a; j < memo['2'].size(); j++) {
      b = upper_bound(memo['3'].begin(),memo['3'].end(),memo['2'][j])-memo['3'].begin();
      res += memo['3'].size()-b;
    }
  }
  cout << res << "\n";
  return 0;
}
