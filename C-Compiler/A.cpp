#include <bits/stdc++.h>
using namespace std;

int main() {
  http://127.0.0.1/titip-absen/
  ios_base::sync_with_stdio(0);
  int x, y, a, b, c, m;
  map<pair<int,int>,int> hp;
  vector<pair<int,int>> pos;
  cin >> x >> y;
  m = 0;
  for (int i = 0; i < 5; i++) {
    cin >> a >> b >> c;
    hp[{a,b}] = c;
    pos.push_back({a,b});
    if (pow(a-x,2) + pow(b-y,2) <= 25) m++;
  }
  int creep;
  cin >> creep;
  for (int i = 0; i < creep; i++) {
    cin >> a >> b;
    if (pow(a-x,2) + pow(b-y,2) <= 25) m++;
  }
  string temp;
  int k;
  cin >> temp;
  if (temp == "YA")
    k = 140;
  else
    k = 70;
  int damage = 270 + m*k;
  int dead = 0;
  for (int i = 0; i < 5; i++) {
    if (pow(pos[i].first-x,2) + pow(pos[i].second-y,2) > 25) continue;
    if (damage >= hp[{pos[i].first,pos[i].second}]) dead++;
  }
 vector<string> loud = {"NOOB", "NOT BAD", "DOUBLE KILL",
                 "TRIPLE KILL", "ULTRA KILL",
                 "RAMPAGE"};
  cout << loud[dead] << "\n";
  return 0;
}
