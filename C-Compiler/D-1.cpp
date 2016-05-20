#include <bits/stdc++.h>
using namespace std;

int main() {
  http://127.0.0.1/titip-absen/
  ios_base::sync_with_stdio(0);
  string s;
  cin >> s;
  if (s == "QQQ")
    cout << "Cold Snap\n";
  else if (s == "WWW")
    cout << "EMP\n";
  else if (s == "EEE")
    cout << "Sun Strike\n";
  else if (s == "QQW" || s == "QWQ" || s == "WQQ")
    cout << "Ghost Walk\n";
  else if (s == "QQE" || s == "QEQ" || s == "EQQ")
    cout << "Ice Wall\n";
  else if (s == "WWQ" || s == "WQW" || s == "QWW")
    cout << "Tornado\n";
  else if (s == "WWE" || s == "WEW" || s == "EWW")
    cout << "Alacrity\n";
  else if (s == "EEQ" || s == "EQE" || s == "QEE")
    cout << "Forged Spirit\n";
  else if (s == "EEW" || s == "EWE" || s == "WEE")
    cout << "Chaos Meteor\n";
  else if (s == "QWE" || s == "QEW" || s == "WQE" || s == "WEQ" ||
           s == "EQW" || s == "EWQ")
    cout << "Deafening Blast\n";
  else
    cout << "ERROR : " << s << " NOT FOUND\n";
  return 0;
}
