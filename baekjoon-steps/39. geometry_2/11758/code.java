import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x1 = Integer.parseInt(st.nextToken()), y1 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int x2 = Integer.parseInt(st.nextToken()), y2 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int x3 = Integer.parseInt(st.nextToken()), y3 = Integer.parseInt(st.nextToken());

        x2 -= x1; y2 -= y1; x3 -= x1; y3 -= y1;

        int res = 0; // 시계: -1, 반시계: 1, 일직선: 0

        if (x2 == 0) { // 수직
            if (y2 > 0) { // 윗방향
                if (x3 > x2) {
                    res = -1;
                } else if (x3 < x2) {
                    res = 1;
                }
            } else { // 아랫방향
                if (x3 < x2) {
                    res = -1;
                } else if (x3 > x2) {
                    res = 1;
                }
            }
        } 
        else if (y2 == 0) { // 수평
            if (x2 > 0) { // 오른쪽
                if (y3 > y2) {
                    res = 1;
                } else if (y3 < y2) {
                    res = -1;
                }
            } else { // 왼쪽
                if (y3 < y2) {
                    res = 1;
                } else if (y3 > y2) {
                    res = -1;
                }
            }
        }
        else { // 수직 / 수평이 아닌 기울기
            if (y2 * (x3 - x2) > x2 * (y3 - y2)) res = -1;
            else if (y2 * (x3 - x2) < x2 * (y3 - y2)) res = 1;
        }

        bw.write(res + "\n");
        bw.close();
        br.close();
    }
}