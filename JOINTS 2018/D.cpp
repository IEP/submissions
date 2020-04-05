#include <bits/stdc++.h>
using namespace std;

int main() {
   int t;
   cin >> t;
   for (int i = 0; i < t; i++) {
       long long n;
       cin >> n;
       cout << "Kasus #" << i+1 << ": ";
       if (n % 10 == 6) cout << "6\n";
       else if (n == 3) cout << "9\n";
       else if (n % 10 == 0) cout << "0\n";
       else if (n % 10 == 1) cout << "1\n";
       else if (n % 10 == 2) cout << "2\n";
       else if (n % 10 == 3) cout << "1\n";
       else if (n % 10 == 4) cout << "4\n";
       else if (n % 10 == 5) cout << "5\n";
       else if (n % 10 == 7) cout << "1\n";
       else if (n % 10 == 8) cout << "8\n";
       else if (n % 10 == 9) cout << "1\n";
   }
   return 0;
}
