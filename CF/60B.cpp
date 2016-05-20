#include <bits/stdc++.h>
using namespace std;

int k, n, m, a, b;
vector<vector<int>> cur;
char cell[15][15][15];

int floodFill() {
  int score = 0, x, y, z;
  vector<int> p;
  map<vector<int>,bool> visited;
  queue<vector<int>> q; q.push({0,a-1,b-1});
  while (!q.empty()) {
    p = q.front(); q.pop();
    if (!visited[p]) {
      score++;
      visited[p] = 1;
      for (int i = 0; i < 6; i++) {
        z = p[0] + cur[i][0];
        y = p[1] + cur[i][1];
        x = p[2] + cur[i][2];
        if (0 <= z && z < k && 0 <= y && y < n && 0 <= x && x < m) {
          if (cell[z][y][x] == '.') {
            q.push({z,y,x});
          }
        }
      }
    }
  }
  return score;
}

int main() {
  ios_base::sync_with_stdio(0);
  string temp;
  cur = {{-1,0,0},{1,0,0},{0,-1,0},{0,1,0},{0,0,-1},{0,0,1}};
  cin >> k >> n >> m;
  for (int i = 0; i < k; i++)
    for (int j = 0; j < n; j++)
      cin >> cell[i][j];
  cin >> a >> b;
  cout << floodFill() << "\n";
  return 0;
}
