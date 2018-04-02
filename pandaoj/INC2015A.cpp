#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, N, counter, temp;
    cin >> T;
    for (int i = 0; i < T; i++) {
        counter = 0;
        cin >> N;
        for (int j = 0; j < N; j++) {
            cin >> temp;
            if (temp < 60) counter++;
        }
        printf("Case #%d: %d\n", i+1, counter);
    }
    return 0;
}