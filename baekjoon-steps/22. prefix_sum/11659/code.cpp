#include <iostream>
using namespace std;

int main() {
    // 아래 두 줄의 코드가 시간 초과가 뜨냐 안뜨냐를 결정함ㄴ
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    int n, m;
    cin >> n >> m;
    long long arr[100001] = {0};
    for (int i = 1; i <= n; i++) {
        long long a;
        cin >> a;
        arr[i] += a + arr[i-1];
    }
    for (int i = 0; i < m; i++) {
        int s, e;
        cin >> s >> e;
        cout << arr[e] - arr[s-1] << '\n';
    }
    return 0;
}

/*
n, m = map(int, input().split())
pre_sum = [0] + list(map(int, input().split()))

for i in range(2, n+1):
    pre_sum[i] += pre_sum[i-1]

for _ in range(m):
    i, j = map(int, input().split())

    print(pre_sum[j] - pre_sum[i-1])
*/