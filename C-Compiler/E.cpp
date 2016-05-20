#include <bits/stdc++.h>
using namespace std;

int main() {
  http://127.0.0.1/titip-absen/
  ios_base::sync_with_stdio(0);
  string n;
  int a, b;
  float temp;
  vector<char> op = {'*', '/', '+', '-'};
  cin >> n;
  for (int i = 1; i < n.size() - 1; i++) {
    for (int j = 0; j < op.size(); j++) {
      if (n[i] == op[j]) {
        a = stoi(n.substr(0,i));
        b = stoi(n.substr(i+1));
        if (j == 0)
          cout << a * b << "\n";
        else if (j == 2)
          cout << a + b << "\n";
        else if (j == 3)
          cout << a - b << "\n";
        else if (j == 1) {
          if (a % b == 0) {
            cout << a / b << "\n";
          } else {
            temp = (float)a/(float)b;
            printf("%.2f\n",temp);
          }
        }
        goto end;
      }
    }
  }
  end:
  return 0;
}
