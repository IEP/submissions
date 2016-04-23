#include <bits/stdc++.h>
using namespace std;

int main () {
  int N, M, c = 0, partial = 0, firstEnd, secondEnd, reminder, res;
  vector<int> pList;
  cin >> N >> M;
  while (partial < N) {
    c++;
    partial += pow(M,c);
    pList.push_back(partial);
  }
  c--;
  cout << c << "\n";
  firstEnd = pList[pList.size() - 2];
  secondEnd = pList[pList.size() - 1];
  reminder = N - firstEnd;
  // printf("%d %d %d %d %d\n", firstEnd, secondEnd, reminder, c, (int)pow(M,c));
  return 0;
}
