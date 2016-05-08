#include <bits/stdc++.h>
using namespace std;
int main () {
  ios_base::sync_with_stdio(0);
  int N, pos;
  string s, temp;
  cin >> s;
  pos = s.find("*");
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> temp;
    if (s != "*") {
      //cout << "rear slice: " << temp.substr(temp.size()-(s.size()-pos-1)) << "\n";
      //cout << "front slice: " << temp.substr(0,pos) << "\n";
      if (pos == 0) {
        if (temp.substr(temp.size()-s.size()+1) == s.substr(1)) {
          cout << temp << "\n";
        }
      } else if (pos == s.size()-1) {
        if (temp.substr(0,s.size()-1) == s.substr(0,s.size()-1)) {
          cout << temp << "\n";
        }
      } else {
        if (temp.substr(0,pos) == s.substr(0,pos) &&
            temp.substr(temp.size()-(s.size()-pos-1)) == s.substr(pos+1)) {
          cout << temp << "\n";
        }
      }
    } else {
      cout << temp << "\n";
    }
  }
  return 0;
}
