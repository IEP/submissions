#include <bits/stdc++.h>
using namespace std;

int bounceCount(bool top[120], bool bottom[120], int target) {
    int counter = 0;
    for (int i = target; i < 120; i += target) {
        if ((i / target) % 2 == 1) {
            if (top[i]) {
                counter++;
            } else {
                return counter;
            }
        } else {
            if (bottom[i]) {
                counter++;
            } else {
                return counter;
            }
        }
    }
    return counter;
}

int main() {
    int TCcount;
    scanf("%d", &TCcount);
    for (int TC = 1; TC < TCcount + 1; TC++) {
        printf("Kasus %d:\n", TC);
        int topMirror, bottomMirror, shoot;
        bool topBouncer[120], bottomBouncer[120];
        memset(&topBouncer, 0, sizeof(topBouncer));
        memset(&bottomBouncer, 0, sizeof(bottomBouncer));
        scanf("%d", &topMirror);
        for (int i = 0; i < topMirror; i++) {
            int start, end;
            scanf("%d %d", &start, &end);
            for (int j = 0; j <= end; j++) {
                topBouncer[start + j] = 1;
            } 
        }
        scanf("%d", &bottomMirror);
        for (int i = 0; i < bottomMirror; i++) {
            int start, end;
            scanf("%d %d", &start, &end);
            for (int j = 0; j <= end; j++) {
                bottomBouncer[start + j] = 1;
            }
        }
        scanf("%d", &shoot);
        for (int i = 0; i < shoot; i++) {
            int target;
            scanf("%d", &target);
            printf("%d\n", bounceCount(topBouncer, bottomBouncer, target));
        }
#ifndef ONLINE_JUDGE
        for (int i = 0; i < 120; i++) {
            if (topBouncer[i])
                printf("1");
            else
                printf("0");
        }
        printf("\n");
        for (int i = 0; i < 120; i++) {
            if (bottomBouncer[i])
                printf("1");
            else
                printf("0");
        }
        printf("\n");
#endif
    }
    return 0;
}