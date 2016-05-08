#include <bits/stdc++.h>
using namespace std;

int M, N, maks;
char board[25][25];
char copyBoard[25][25];
vector<pair<vector<pair<int,int>>,int>> region;
map<pair<int,int>,bool> globalVisit;
vector<pair<int,int>> floodCursor;

pair<int,vector<pair<int,int>>> floodFill(int r, int c, int mode) {
  int x, y;
  pair<int,int> pos;
  map<pair<int,int>,bool> visited;
  queue<pair<int,int>> q; q.push({r,c});
  char color = board[r][c];
  while (!q.empty()) {
    pos = q.front(); q.pop();
    if (!visited[{pos.first,pos.second}]) {
      visited[{pos.first,pos.second}] = 1;
      globalVisit[{pos.first,pos.second}] = 1;
      for (int i = 0; i < 4; i++) {
        y = pos.first + floodCursor[i].first;
        x = pos.second + floodCursor[i].second;
        if (0 <= y && y < M && 0 <= x && x < N) {
          if (board[y][x] == color)
            q.push({y,x});
        }
      }
    }
  }
  auto T = (int)visited.size();
  vector<pair<int,int>> temp;
  if (color == '.') {
    T = 0;
  } else {
    T = T * (T - 1);
  }
  if (mode == 1) {
    for (auto a : visited)
      if (a.second)
        temp.push_back({a.first.first,a.first.second});
    region.push_back({temp, T});
  }
  pair<int,vector<pair<int,int>>> result = {T, temp};
  return result;
}

void runtuh(vector<pair<int,int>> dot) {
  for (auto a : dot) {
    board[a.first][a.second] = '.';
  }
  for (int j = 0; j < N; j++) {
    for (int i = M - 1; i > -1; i--) {
      if (board[i][j] == '.') {
        for (int k = i; k > 0; k--) {
          for (int l = k - 1; l >= 0; l--) {
            if (board[k][j] == '.' && board[l][j] != '.')
              swap(board[k][j], board[l][j]);
          }
        }
        break;
      }
    }
  }
}

int main() {
  ios_base::sync_with_stdio(0); cin.tie(0);
  cin >> M >> N;
  int score;
  pair<int,vector<pair<int,int>>> temp;
  vector<pair<int,int>> area;
  maks = 0;
  floodCursor = {{-1,0},{0,-1},{0,1},{1,0}};
  for (int i = 0; i < M; i++)
    for (int j = 0; j < N; j++)
      cin >> board[i][j];
  for (int i = 0; i < M; i++)
    for (int j = 0; j < N; j++)
      if (!globalVisit[{i,j}])
        floodFill(i,j,1);
  memcpy(copyBoard, board, sizeof board);
  for (auto a : region) {
    if (a.second > 0) {
      memcpy(board, copyBoard, sizeof copyBoard);
      runtuh(a.first);
      score = a.second;
      globalVisit.clear();
      for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++)
          if (!globalVisit[{i,j}])
            maks = max(maks, floodFill(i,j,0).first + score);
    }
  }
  cout << maks << "\n";
  return 0;
}
