import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    static int N;
    static int[][] memo = new int[20][0b100000000000000000000];
    static int[][] dMatrix;
    static int visited;

    static int dfs(int step) {
        if (step == N) return 0;

        if (memo[step][visited] > 0) return memo[step][visited];

        int minV = 20000000;
        
        for (int i = 0; i < N; i++) {
            if (((visited >> i) & 1) == 1) continue;
            visited |= (1 << i);

            int value = dMatrix[step][i] + dfs(step + 1);
            minV = Math.min(minV, value);
            
            visited &= ~(1 << i);
        }
        
        memo[step][visited] = minV;
        
        return minV;
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        dMatrix = new int[20][20];
        
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int d = Integer.parseInt(st.nextToken());
                dMatrix[i][j] = d;
            }
        }

        int minV = dfs(0);
        bw.write(String.format("%d", minV));

        bw.flush();
        bw.close();
    }
}