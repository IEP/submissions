#include <bits/stdc++.h>
using namespace std;

int main() {
   int t;
   cin >> t;
   for (int T = 0; T < t; T++) {
       cout << "Kasus #" << T+1 << ": ";
       int n, m, d;
       cin >> n >> m;
       vector<int> semut, v1, v2, v;
       for (int i = 0; i < n; i++) {
           semut.push_back(i+1);
       }
       for (int i = 0; i < m; i++) {
           vector<int>::const_iterator s = semut.begin();
           cin >> d;
           int mmin = min(d, n);
        //    vector<int> v1(s, s+mmin);
           v1.resize(s, s+mmin);
           if (d < n) {
            //    vector<int> v2(s+mmin, s+n);
            //    vector<int> v;
               
               reverse(v1.begin(), v1.end());
               v.insert(v.end(), v2.begin(),v2.end());
               v.insert(v.end(), v1.begin(), v1.end());
               semut = v;
           }
           else {
               reverse(v1.begin(), v1.end());
               semut = v1;
           }
       }
       for (int i = 0; i < n; i++) {
           cout << semut[i];
           if (i != n-1) cout << " ";
           else cout << "\n";
       }
   }
   return 0;
}

