#include <bits/stdc++.h>
using namespace std;

long long factorial(long long n) {
  long long result = 1;
  if (n == 0)
    return result;
  for (int i = 1; i <= n; i++)
    result *= i;
  return result;
}

long long combi(long long n, long long k) {
  long long upper = n;
  long long mid = max(n-k,k);
  long long lower = min(n-k,k);
  long long result = upper;
  upper--;
  for (int i = upper; upper > mid; upper--)
    result *= upper;
  result /= factorial(lower);
  if (lower == 0)
    return 1;
  return result;
}

int main() {
  long long n, k;
  while (scanf("%lli %lli", &n, &k) != EOF) {
    if (n == 0 && k == 0)
      break;
    printf("%lli\n",combi(n,k));
  }
  return 0;
}
