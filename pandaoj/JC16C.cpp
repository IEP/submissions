#include <bits/stdc++.h>
using namespace std;

int numFamily;
map<int, vector<int> > familyTree, ancestor;
bitset<1000000> whitelist;

void bfs(int family, int mode) {
    queue<int> q; q.push(family);
    while (!q.empty()) {
        int fam = q.front(); q.pop();
        if (mode == 1 && !whitelist[fam]) {
            whitelist[fam] = 1;
            numFamily--;
        } else if (mode == 2 && whitelist[fam]) {
            whitelist[fam] = 0;
            numFamily++;
        }
        for (int i = 0; i < (int)familyTree[fam].size(); i++) {
            q.push(familyTree[fam][i]);
        }
    }
}

void lowestCommon(int family1, int family2) {
}

void makeAncestorList() {
    
}

int main() {
    int questions;
    whitelist.reset(); // 1 = blacklisted
    scanf("%d", &numFamily);
    for (int i = 0; i < numFamily - 1; i++) {
        int upperGen, lowerGen;
        scanf("%d %d", &upperGen, &lowerGen);
        familyTree[upperGen].push_back(lowerGen);
    }
    makeAncestorList();
    scanf("%d", &questions);
    for (int i = 0; i < questions; i++) {
        int command, family, family2;
        scanf("%d", &command);
        if (command == 3) {
            scanf("%d %d", &family, &family2);
        } else {
            scanf("%d", &family);
        }
        switch (command) {
            case 1:
            case 2:
                bfs(family, command);
                printf("%d\n", numFamily);
                break;
            case 3:
                lowestCommon(family, family2);
                break;
        }
    }
    return 0;
}