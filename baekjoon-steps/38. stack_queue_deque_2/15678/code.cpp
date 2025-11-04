#include <iostream>
#include <deque>
#include <utility>
using namespace std;
typedef long long int ll;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    int N, D;
    cin >> N >> D;

    ll max_score = -1000000000;
    
    deque<pair<int, ll>> dq;
    dq.push_back({0, -1000000000});
    for (int i = 1; i <= N; i++) {
        if (!dq.empty() && dq.front().first < i - D) dq.pop_front();
        ll K;
        cin >> K;
        ll sum = max(dq.front().second + K, K);
        // cout << "sum: " << sum << '\n';
        // cout << "i: " << i << '\n';
        // for (pair<int, ll> elem: dq) {
        //     cout << elem.first << ' ' << elem.second << '\n';
        // }
        // cout << '\n';
        max_score = max(max_score, sum);
        
        while (!dq.empty() && dq.back().second <= sum) dq.pop_back();
        dq.push_back({i, sum});
    }
    cout << max_score;
    return 0;
}
