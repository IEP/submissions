#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int i = 1;
  string s;
  while (cin >> s) {
    if (s == "*") break;
    printf("Case %d: ",i);
    if (s == "Hajj")
      printf("Hajj-e-Akbar\n");
    else
      printf("Hajj-e-Asghar\n");
    i++;
  }
  return 0;
}
