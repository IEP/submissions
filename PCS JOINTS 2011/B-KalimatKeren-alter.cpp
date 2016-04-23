#include <bits/stdc++.h>
using namespace std;

typedef pair<string, int> psi;
typedef vector<string> vs;

int N, result;
string awal, akhir;
map<string, vs> kata;

void dfs() {
  psi qd;
  map<string, bool> visit;
  stack<psi> q; q.push({awal, 1});
  result = 0;
  while (!q.empty()) {
    qd = q.top(); q.pop();
    cout << ">> " << qd.first << " " << qd.second << "\n";
    for (int i = 0; i < (int)kata[qd.first].size(); i++) {
      if (!visit[kata[qd.first][i]]) {
        cout << "* pushing -> " << kata[qd.first][i] << " " << qd.second+1 << "\n";
        visit[kata[qd.first][i]] = 1;
        q.push({kata[qd.first][i], qd.second+1});
      }
    }
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  kata = {{"lho", {"keren", "kul"}},
          {"keren", {"lho", "parah"}},
          {"kul", {"parah"}},
          {"parah", {"lho"}}};
  cin >> N >> awal >> akhir;
  result = 0;
  dfs();
  cout << result << "\n";
  return 0;
}
