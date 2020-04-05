#include <bits/stdc++.h>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
      int N, M, depth;
      queue<int> q;
    
      cin >> N >> M;
      for (int j = 1; j <= N; j++) {
          q.push(j);
      }
      for (int j = 0; j < M; j++) {
          queue<int> q_temp;
          stack<int> s;

          cin >> depth;
          for (int k = 0; k < min(depth, N); k++) {
              int temp = q.front(); q.pop();
              s.push(temp);
          }
          while (!q.empty()) {
              int temp = q.front(); q.pop();
              q_temp.push(temp);
          }
          while (!s.empty()) {
              int temp = s.top(); s.pop();
              q_temp.push(temp);
          }
          q = q_temp;
      }
      cout << "Kasus #" << i << ": ";
      while (!q.empty()) {
          int temp = q.front(); q.pop();
          cout << temp;
          if (!q.empty()) {
              cout << " ";
          } else {
              cout << "\n";
          }
      }
  }
  return 0;
}
