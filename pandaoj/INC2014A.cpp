#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, N, space, res, temp;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        scanf("%d", &N);
        space = 0;
        for (int j = 0; j < N; j++) {
            scanf("%d", &temp);
            space += temp;
        }
        space /= 1000;
        res = pow(2, ceil(log2(space)));
        printf("Case #%d: %dGB\n", i + 1, res);
    }
    return 0;
}