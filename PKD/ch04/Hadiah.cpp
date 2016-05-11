#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

LL A, B, C, N, res, temp;
pair<LL,bool> visited;
pair<LL,LL> memo;

int main() {
  ios_base::sync_with_stdio(0);
  cin >> A >> B >> C >> N;
  temp = pow_mod(A,pow(B,C));
  return 0;
}
