#include <bits/stdc++.h>
using namespace std;

int main() {
   int t, k, koin;
   cin >> k;
   long long f[10010], coin[k];
   vector<int> res, temp;
   for (int i = 0; i < k; i++) {
       cin >> coin[i];
   }
   f[0] = 0;
   cin >> t;
   for (int i = 1; i <= 10001; i++) {
       long long best = INT_MAX;
       f[i] = -1;
       for (int j = 0; j < k; j++) {
           if (i - coin[j] >= 0)
               if (best > f[i-coin[j]]) {
                   best = f[i-coin[j]];
                   koin = coin[j];   
               }
       }
       f[i] = best + 1;
       temp.push_back(koin);
       res.push_back(temp[koin]);
   }
   for (int i = 0; i < t; i++) {
       int l;
       cin >> l;
       cout << "Kasus #" << i+1 << ": ";
       if (f[l] == 2147483648) cout << "Tidak mungkin\n";
       else cout << f[l] << "\n";
   }
   return 0;
}