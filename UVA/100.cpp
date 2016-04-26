#include <bits/stdc++.h>
using namespace std;
int main() {
  int i, j;
  while (scanf("%d %d", &i, &j) != EOF) {
    int cycle = 1;
    for (int a = min(i,j); a <= max(i,j); a++) {
      int c = 1, n = a;
      while (n != 1) {
        if (n % 2 == 0)
          n = n/2;
        else
          n = 3*n + 1;
        c++;
      }
      if (c > cycle)
        cycle = c;
    }
    printf("%d %d %d\n", i, j, cycle);
  }
  return 0;
}
