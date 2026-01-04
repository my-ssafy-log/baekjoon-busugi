import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    // 좌표평면에서 (-a, 0)과 (0, c)를 지나는 직선이 (b / sqrt(2))를 넘는지 확인 (볼록한지 확인)
    static boolean isOK(int a, int b, int c) {
        // y = (c/a)x + c;
        // y = -x;
        // -x = (c/a)x + c;
        // -c = (c/a)x + x;
        // -c = (c/a + 1)x;
        // -c / (c/a + 1) = x;
        // x = -c / (c/a + 1);
        
        double x = (double)c / ((double)c/(double)a + 1);
        return x * Math.sqrt(2) < b;
    }

    static int cases = 0;
    static int[] arr = new int[8];
    static boolean[] visited = new boolean[8];
    static int[] selections = new int[8];

    static void choose(int step) {
        if (step == 8) {
            for (int i = 0; i < 8; i++) {
                int a = selections[i], 
                    b = selections[(i+1) % 8],
                    c = selections[(i+2) % 8];

                if (!isOK(a, b, c)) {
                    return;
                }
            }
            cases += 1;
            return;
        }

        for (int i = 0; i < 8; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            selections[step] = arr[i];
            choose(step + 1);
            visited[i] = false;
        }
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i = 0; i < 8; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        choose(0);
        
        System.out.println(cases);
    }
}