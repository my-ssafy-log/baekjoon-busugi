import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static boolean isOK(int a, int b, int c) {
        double x1 = a,
            y1 = 0,
            x2 = b / Math.sqrt(2),
            y2 = b / Math.sqrt(2),
            x3 = 0,
            y3 = c;
        double S = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3;
        return S >= 0;
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