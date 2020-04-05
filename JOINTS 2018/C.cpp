#include <bits/stdc++.h>
using namespace std;

int main() {
   int t;
   cin >> t;
   for (int i = 0; i < t; i++) {
       int a, b, c, d, e;
       cin >> a >> b >> c >> d >> e;
       cout << "Kasus #" << i+1 << ": ";
       if (pow((d-a), 2) + pow((e-b), 2) > c*c) cout << "Tidak kena\n";
       else cout << "Kena\n";
   }   
   return 0;
}
