#include <bits/stdc++.h>
using namespace std;

double R, H, h, a, area, pi, temp;

inline double f(double x) {
  return 1.0/3.0*pi*x*x*x*R/H*R/H + pi*x*x*R/H*sqrt(R/H*R/H+1) - area;
}

int main() {
  int T;
  pi = 2*acos(0.0);
  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> R >> H;
    area = 2*pi*R*sqrt(R*R+H*H);
    if (area/2 > 1.0/3.0*pi*R*R*H) {
      printf("%.6lf\n",H);
    } else {
      a = H;
      h = 0;
      while (1) {
        temp = h;
        h = h-(f(h)*(h-a))/(f(h)-f(a));
        a = temp;
        if (abs(f(h)) <= 1e-6)
          break;
      }
      printf("%.6lf\n",h);
    }
  }
  return 0;
}
