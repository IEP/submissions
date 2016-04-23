#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
map<LL,bool> visited;
map<LL,pair<LL,LL>> memo;
long long A;

pair<LL,LL> pangkat(LL N) {
  pair<LL,LL> x, y;
  if (visited[N]) return memo[N];
  x = pangkat(N/2);
  y = pangkat(N-N/2);
  visited[N] = 1;
  memo[N] = {(x.first * y.first) % 1000000, (x.second * y.second) % 1000000007};
  return memo[N];
}

int main() {
  long long B;
  pair<LL,LL> temp;
  string result;
  cin >> A >> B;
  visited = {{0,1},{1,1}};
  memo = {{0,{1,1}},
          {1,{A % 1000000, A % 1000000007}}};
  temp = pangkat(B);
  result = to_string(temp.first);
  if (temp.first != temp.second) {
    while (result.size() < 6)
      result = "0" + result;
  }
  cout << result << "\n";
  return 0;
}
