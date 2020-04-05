#include <bits/stdc++.h>
using namespace std;

int main() {
   int t;
   cin >> t;
   for (int i = 0; i < t; i++) {
       int n, b;
       cin >> b >> n;
       cout << "Kasus #" << i+1 << ": ";
       if (b % n == 1) cout << "Bisa\n";
       else cout << "Tidak bisa\n";
   }
   return 0;
}