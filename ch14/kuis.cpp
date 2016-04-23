#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

LL banyak(LL x) {
  if (x < 0)
    return 0;
  else
    return x + banyak(x - 2);
}
void draw(LL x) {
  if (x > 0) {
    draw(x-1);
    for (LL i = 0; i < x; i++) {
      cout << "*";
    }
    cout << "\n";
  }
}

LL jabatan(LL a, LL b) {
  LL temp;
  if (b == 0)
    return 1;
  else if (b % 2 == 1)
    return a * jabatan(a, b-1);
  else {
    temp = jabatan(a, b/2);
    return temp * temp;
  }
}

LL kardus(LL a, LL b) {
  if (a > b)
    return 1 + kardus(a-1,b);
  else if (a < b)
    return 1 + kardus(a,b-1);
  else
    return a + b;
}

LL ekor(LL a, LL b, LL t) {
  if (b == 0)
    return t;
  else
    return ekor(a,b-1,t*a);
}

void majuMundur(string str, LL i) {
  if (i == str.size())
    cout << str[i];
  else {
    cout << str[i];
    majuMundur(str, i+1);
    cout << str[i];
  }
}
 /**
inline LL ping(LL a) {
  if (a == 0)
    return 0;
  else
    return 1 + pong(a-1);
}

inline LL pong(LL a) {
  if (a == 0)
    return 0;
  else
    return 2 + ping(a-1);
}
**/
string wolo(string s) {
  string t;
  if (s.size() == 0)
    return "";
  else {
    t = s;
    t.erase(1,1);
    return wolo(t) + s[1];
  }
}

int main() {
  //cout << ping(5) << "\n";
  cout << wolo("dengklek") << "\n";
  return 0;
}
