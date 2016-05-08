#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int N;
  long long B, temp;
  vector<long long> H, sH;
  //cin >> N >> B;
  scanf("%d %lld",&N,&B);
  for (int i = 0; i < N; i++) {
    //cin >> temp;
    scanf("%lld",&temp);
    H.push_back(temp);
  }
  sort(H.rbegin(),H.rend());
  sH.push_back(H[0]);
  for (int i = 1; i < N; i++) {
    sH.push_back(H[i] + sH[i-1]);
    if (sH[i] >= B) break;
  }
  //cout << lower_bound(sH.begin(),sH.end(),B) - sH.begin() + 1 << "\n";
  temp = (long long)(lower_bound(sH.begin(),sH.end(),B) - sH.begin() + 1);
  printf("%lld\n",temp);
  return 0;
}
