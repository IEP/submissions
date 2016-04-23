#include <bits/stdc++.h>
using namespace std;

map<string,int> buku;
int cari(string nama) {
  if (buku.find(nama) != buku.end()) {
    return buku[nama];
  } else {
    return 0;
  }
}

int main() {
  int n,q,no;
  string nama;
  cin >> n >> q;
  for (int i = 0; i < n; i++) {
    cin >> nama >> no;
    buku[nama] = no;
  }
  for (int i = 0; i < q; i++) {
    cin >> nama;
    if (cari(nama) != 0) {
      cout << cari(nama) << "\n";
    } else {
      cout << "NIHIL\n";
    }
  }
  return 0;
}
