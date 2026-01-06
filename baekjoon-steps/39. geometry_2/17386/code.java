import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static long getCCW(long x1, long y1, long x2, long y2, long x3, long y3) {
        return x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3;
    }

    static boolean isOK(long S1, long S2) {
        return (S1 == 0 && S2 != 0) || 
            (S1 != 0 && S2 == 0) || 
            (S1 < 0 && S2 > 0) || 
            (S1 > 0 && S2 < 0);
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        long x1 = Long.parseLong(st.nextToken()),
            y1 = Long.parseLong(st.nextToken()),
            x2 = Long.parseLong(st.nextToken()),
            y2 = Long.parseLong(st.nextToken());
        
        st = new StringTokenizer(br.readLine());

        long x3 = Long.parseLong(st.nextToken()),
            y3 = Long.parseLong(st.nextToken()),
            x4 = Long.parseLong(st.nextToken()),
            y4 = Long.parseLong(st.nextToken());

        long S1 = getCCW(x1, y1, x2, y2, x3, y3);
        long S2 = getCCW(x1, y1, x2, y2, x4, y4);
        long S3 = getCCW(x3, y3, x4, y4, x1, y1);
        long S4 = getCCW(x3, y3, x4, y4, x2, y2);
        if (isOK(S1, S2) && isOK(S3, S4)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}