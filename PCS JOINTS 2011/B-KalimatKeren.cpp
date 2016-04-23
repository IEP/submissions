#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<string, LL> psLL;
typedef vector<string> vs;

LL N, res;
string awal, akhir;

map<string, vs> kata;

void dfs() {
  psLL temp;
  map<string, bool> visit;
  string temp1;
  stack<psLL> q; q.push({awal, 1});
  res = 0;
  if (N >= 2)
  while (!q.empty()) {
    temp = q.top(); q.pop();
    cout << temp.first << " " << temp.second << "\n";
    if (temp.second == N && temp.first == akhir) {
      res = (res+1) % 1000000007;
    } else if (temp.second < N) {
      for (long long i = 0; i < (long long)kata[temp.first].size(); i++) {
        if (!visit[temp.first]) {
          q.push({kata[temp.first][i], temp.second+1});
          visit[temp.first] = 1;
        }
      }
    }
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  kata = {{"lho", {"keren", "kul"}},
          {"keren", {"lho", "parah"}},
          {"kul", {"parah"}},
          {"parah", {"lho"}}};
  cin >> N;
  cin >> awal >> akhir;
  dfs();
  cout << res << "\n";
  return 0;
}

