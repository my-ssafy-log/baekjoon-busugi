#include <iostream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

typedef pair<int, int> pos_type;

int n, cnt = 0;
vector<pos_type> pos_v;

void f(int line) {
  if (line == n) {
    cnt++;
    return;
  }
  for (int column = 0; column < n; column++) {
    bool is_valid = true;
    for (pos_type pos : pos_v) {
      if (
        pos.second == column ||
        abs(pos.first - line) == abs(pos.second - column)
      ) {
        is_valid = false;
      }
    }
    
    if (is_valid) {
      pos_v.push_back({line, column});
      f(line + 1);
      pos_v.pop_back();
    }
  }
}

int main() {
  cin.tie(NULL);
  ios_base::sync_with_stdio(false);

  cin >> n;
  for (int column = 0; column < n; column++) {
    pos_v.push_back({0, column});
    f(1);
    pos_v.pop_back();
  }
  cout << cnt;
  return 0;
}