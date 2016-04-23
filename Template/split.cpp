#include <bits/stdc++.h>
using namespace std;

vector<string> splitter(string str) {
  vector<string> o;
  stringstream ss(str);
  string temp;
  while (ss >> temp)
    o.push_back(temp);
  return o;
}

int main() {
  string kalimat;
  getline(cin, kalimat);
  vector<string> kata = splitter(kalimat);
  for (auto &it: kata)
    cout << it << "\n";
  return 0;
}
