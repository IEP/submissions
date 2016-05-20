#include <bits/stdc++.h>
using namespace std;

int main() {
  string skill;
  cin >> skill;
  vector<string> legal = {"QQQ", "QQW", "QQE", "WWW",
                          "WWQ", "WWE", "EEE", "EEQ",
                          "EEW", "QWE"};
  map<string,string> out = {{"QQQ","Cold Snap"}, {"QQW","Ghost Walk"},
                            {"QQE","Ice Wall"}, {"WWW","EMP"},
                            {"WWQ","Tornado"}, {"WWE","Alacrity"},
                            {"EEE","Sun Strike"}, {"EEQ","Forged Spirit"},
                            {"EEW","Chaos Meteor"}, {"QWE","Deafening Blast"}};
  bool flag = 0;
  for (int i = 0; i < legal.size(); i++) {
    if (legal[i] == skill) {
      flag = 1;
      break;
    }
  }
  if (flag)
    cout << out[skill] << "\n";
  else
    cout << "ERROR : " << skill << " NOT FOUND \n";
  return 0;
}
