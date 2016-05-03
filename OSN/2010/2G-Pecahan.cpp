#include <bits/stdc++.h>
using namespace std;

int main() {
  int K, temp;
  vector<int> money = {1,2,5,10,20,50,100,200,500,1000};
  reverse(money.begin(),money.end());
  cin >> K;
  for (int i = 0; i < money.size(); i++) {
    if (K >= money[i]) {
      temp = K / money[i];
      cout << money[i] << " " << temp << "\n";
      K -= temp * money[i];
    } else if (K == 0) break;
  }
  return 0;
}
