#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int n;
  string s, spell;
  vector<string> mantra;
  cin >> s >> n;
  mantra.resize(n);
  for (int i = 0; i < n; i++)
    cin >> mantra[i];
  spell = "";
  for (int i = 0; i < (int)s.size(); i++) {
    spell += s[i];
    for (int j = 0; j < n; j++) {
      if ((int)spell.size() >= (int)mantra[j].size()) {
        if (spell.substr((int)(spell.size()-mantra[j].size()),
            mantra[j].size()) == mantra[j])
          spell = spell.substr(0,(int)(spell.size()-mantra[j].size()));
      }
    }
  }
  cout << spell << "\n";
  return 0;
}
