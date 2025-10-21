#include <iostream>
#include <climits>
using namespace std;

typedef struct Matrix {
    int r;
    int c;
} Matrix;

Matrix matrixes[500];
int memo[500][500];

int dfs(int start, int end) {
    // if (start == end-1) {
    //     memo[start][end] = matrixes[start].r * matrixes[end].r * matrixes[end].c;
    //     return matrixes[start].r * matrixes[end].r * matrixes[end].c;
    // }
    // left.r * right.r * right.c + memo[a][b] + memo[c][d]
    // a,  b,  c,  d
    // memo[a][b] +
    // memo[c][d]

    
    if (start == end) {
        return 0;
    }

    if (memo[start][end] != -1) {
        return memo[start][end];
    }

    memo[start][end] = INT_MAX;
    for (int mid = start + 1; mid <= end; mid++) {
        int left = dfs(start, mid-1);
        int right = dfs(mid, end);
        memo[start][end] = min(
            memo[start][end],
            matrixes[start].r * matrixes[mid].r * matrixes[end].c + left + right
        );
    }
    return memo[start][end];
}

/*
C1 C2  //  C3
C1.r * C2.r * C2.c
C1 C2   +   C1.r * C3.r * C3.c

C1 // C2 C3
C1.r * (C2@C3).r  +  C2 C3
*/
    

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    freopen("input.txt", "r", stdin);

    fill_n(&memo[0][0], 500*500, -1);
    
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> matrixes[i].r >> matrixes[i].c;
    }
    cout << dfs(0, N-1);
}