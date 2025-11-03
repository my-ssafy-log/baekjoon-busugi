#include <iostream>
#include <deque>
#include <utility>
using namespace std;

int N, K;
deque<pair<int, long long int>> dq;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    dq.push_back({0, 0});

    cin >> N >> K;
    long long int min_sum = -1;
    long long total_sum = 0;
    
    for (int i = 1; i <= N; i++) {
        // i번 소를 비활성화 한다고 하면 K연속 안되게 하는 최적으로 비활성화한 소와 합을 더함
        // 만약 i번 소를 비활성화하는데 범위 밖의 소는 deque에서 pop_front해서 없앰 -> 그 소는 K개 이하로 연속되어야 한다는 조건을 위배하게 만들 수 있기 때문
        if (!dq.empty() && i - 1 - dq.front().first > K) dq.pop_front();

        int eff;
        cin >> eff;
        total_sum += eff;
        long long int optimized_sum = dq.front().second + eff;

        if (i >= N - K && (min_sum == -1 || min_sum > optimized_sum)) {
            min_sum = optimized_sum;
        }
        
        while (!dq.empty() && dq.back().second >= optimized_sum) dq.pop_back();
        dq.push_back({i, optimized_sum});
    }
    if (N == K || min_sum == -1) min_sum = 0;
    cout << total_sum - min_sum;
    return 0;
}