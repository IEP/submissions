#include <bits/stdc++.h>
using namespace std;

int main () {
  //ios_base::sync_with_stdio(0);
  int N;
  string temp = "";
  scanf("%d\n", &N);
  for (int i = 0; i < N; i++) {
    getline(cin, temp);
    stringstream ss(temp);
    vector<string> words;
    string w;
    while (ss >> w) {
      words.push_back(w);
    }
    reverse(words.begin(), words.end());
    printf("Case #%d: ", i+1);
    for (int j = 0; j < words.size(); j++) {
      cout << words.at(j);
      if (j < words.size() - 1)
        cout << " ";
    }
    cout << "\n";
  }
  return 0;
}
