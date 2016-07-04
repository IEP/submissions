#include <bits/stdc++.h>
using namespace std;

map<unsigned long long,bool> visited;
map<unsigned long long,int> co;

int collatz(unsigned long long n) {
  if (visited[n])
    return co[n];
  int res = 1;
  if (n > 1)
    if (n % 2 == 0)
      res += collatz(n/2);
    else
      res += collatz(3*n+1);
  visited[n] = 1;
  co[n] = res;
  return res;
}

int main() {
  int res, temp = 0;
  pair<int,int> maks;
  co = {{1,1}};
  visited = {{1,1}};
  maks = {0,0};
  for (int i = 1; i < 1000000; i++) {
    res = collatz(i);
    if (max(res,maks.second) == res && temp != i) {
      maks = {i,res};
      temp = i;
      printf("%d %d\n",i,res);
    }
  }
  return 0;
}
