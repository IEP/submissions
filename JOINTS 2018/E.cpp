#include <bits/stdc++.h>

using namespace std;
int memo[10001];

vector<int> cables;
vector<bool> visited;

int cables_count(int panjang) {
    if (visited[panjang]) {
        return memo[panjang];
    }
    if (panjang <= 0) {
        return INT_MAX;
    }
    int temp = INT_MAX;
    for (auto &i: cables) {
        temp = min(temp, cables_count(panjang-i));
    }
    memo[panjang] = 1 + temp;
    visited[panjang] = true;
    return memo[panjang];
}

int main() {
    int N; // cable kinds
    memset(memo, INT_MAX, sizeof memo);
    cin >> N;
    
    cables.resize(N);
    visited.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> cables[i]; // storing cables;
        memo[i] = cables[i];
    }
    for (int i = 0; i < 10001; i++) {
        
    }
    return 0;
}