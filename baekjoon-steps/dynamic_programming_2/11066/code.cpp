#include <iostream>
#include <vector>
#include <climits>
using namespace std;

long long memo[500][500];
vector<long long> culsum;

long long dfs(int start, int end) {
    if (start == end) {
        return 0;
    }
    
    if (memo[start][end] != -1) {
        return memo[start][end];
    }
    
    long long partsum = culsum[end+1] - culsum[start];
    memo[start][end] = LLONG_MAX;
    
    for (int mid = start + 1; mid <= end; mid++) {
        long long left = dfs(start, mid-1);
        long long right = dfs(mid, end);
        // cout << "left: " << left << ", right: " << right << ", min:" << min(memo[start][end], partsum + left + right) << '\n';
        memo[start][end] = min(memo[start][end], partsum + left + right);
    }
    // cout << "start: " << start << ", end: " << end << ", memo:" << memo[start][end] << '\n';
    
    return memo[start][end];
}

void init_memo() {
    for (int i = 0; i < 500; i++) {
        for (int j = 0; j < 500; j++) {
            memo[i][j] = -1;
        }
    }
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    freopen("input.txt", "r", stdin);

    int T;
    cin >> T;
    
    for (int t = 0; t < T; t++) {
        init_memo();
        
        int K;
        cin >> K;
        
        vector<int> arr(K);
        for (int i = 0; i < K; i++) {
            cin >> arr[i];
        }

        culsum.clear();
        culsum.push_back(0);
        for (int i = 0; i < K; i++) {
            culsum.push_back(culsum.back() + arr[i]);
        }
        
        cout << dfs(0, K-1) << '\n';
    }
    
    return 0;
}