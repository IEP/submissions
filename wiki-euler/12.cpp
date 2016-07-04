#include <bits/stdc++.h>
using namespace std;

int main() {
  int n = 1, add = 2, temp = 0, res;
  pair<int,int> maks;
  maks = {0,0};
  set<int> factor;
  while (1) {
    factor.clear();
    factor.insert(1); factor.insert(n);
    for (int i = 1; i <= n/2+1; i++) {
      if (n % i == 0) {
        factor.insert(i);
        factor.insert(n/i);
      }
    }
    res = (int)factor.size();
    if (max(res,maks.second) == res && res != temp) {
      maks = {n,res};
      temp = res;
      printf("%d %d\n",maks.first,maks.second);
    }
    if (res > 500)
      break;
    n += add;
    add++;
  }
  printf("%d\n",n);
  return 0;
}

// rework: factorize by prime factor
