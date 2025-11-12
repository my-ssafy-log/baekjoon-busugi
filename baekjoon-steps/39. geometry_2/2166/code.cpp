#include <iostream>
#include <utility>
#include <cmath>
using namespace std;

int N;
long long int area = 0;
pair<int, int> points[100000];

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    cin >> N;
    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;
        points[i] = {x, y};
    }
    for (int i = 0; i < N; i++) {
        int next_i = (i + 1) % N;
        
        long long int x1 = points[i].first,
            y1 = points[i].second,
            x2 = points[next_i].first,
            y2 = points[next_i].second;

        area += x1 * y2 - x2 * y1;
    }
    cout << fixed;
    cout.precision(1);
    cout << round(abs(double(area) / 2.0) * 10) / 10;
    return 0;
}