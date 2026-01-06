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

    static boolean isBetween(long a, long b, long c) {
        return a <= b && b <= c;
    }

    static void printPoint(double x, double y) {
        System.out.println(String.format("%.10f %.10f", x, y));
    }

    static void printInterPoint(long x1, long y1, long x2, long y2, long x3, long y3, long x4, long y4) {
        double x, y;
        
        if (x1 == x2) {
            // 만약 첫번째 선분이 x축에 수직이라면
            x = x1;
            double A = (double)(y3 - y4) / (x3 - x4);
            double b = y3 - A * x3;
            y = A * x1 + b;
        } else if (x3 == x4) {
            // 만약 두번째 선분이 x축에 수직이라면
            x = x3;
            double A = (double)(y1 - y2) / (x1 - x2);
            double b = y1 - A * x1;
            y = A * x3 + b;
        } else { 
            // 둘 다 x축에 수직이 아니라면
            double A1 = (double)(y1 - y2) / (x1 - x2);
            double b1 = y1 - A1 * x1;
            double A2 = (double)(y3 - y4) / (x3 - x4);
            double A1MinusA2 = A1 - A2;
            x = ((A1 * x1 - y1) - (A2 * x3 - y3)) / A1MinusA2;
            y = A1 * x + b1;
        }
        printPoint(x, y);
    }

    static void printStraightLineOptional(long x1, long y1, long x2, long y2, long x3, long y3, long x4, long y4) {
        if (x1 == x3 && y1 == y3) {  // 점1이랑 점3이랑 겹친다면
            if (isSameSign(x1 - x2, x4 - x3) && isSameSign(y1 - y2, y4 - y3)) {
                printPoint(x1, y1);
            }
        } else if (x1 == x4 && y1 == y4) {
            if (isSameSign(x1 - x2, x3 - x4) && isSameSign(y1 - y2, y3 - x4)) {
                printPoint(x1, y1);
            }
        } else if (x2 == x3 && y2 == y3) {
            if (isSameSign(x2 - x1, x4 - x3) && isSameSign(y2 - y1, y4 - x3)) {
                printPoint(x2, y2);
            }
        } else if (x2 == x4 && y2 == y4) {
            if (isSameSign(x2 - x1, x3 - x4) && isSameSign(y2 - y1, y3 - x4)) {
                printPoint(x2, y2);
            }
        }
    }

    static boolean isSameSign(long a, long b) {
        return (a < 0 && b < 0) || (a > 0 && b > 0) || (a == 0 && b == 0);
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
            printInterPoint(x1, y1, x2, y2, x3, y3, x4, y4);

        } else if (S1 == 0 && S2 == 0 && S3 == 0 && S4 == 0) {  // 4개의 점이 일직선에 있다면
            long minY = Math.min(y1, y2);
            long maxY = Math.max(y1, y2);
            long minX = Math.min(x1, x2);
            long maxX = Math.max(x1, x2);

            if ((isBetween(minX, x3, maxX) && isBetween(minY, y3, maxY)) || 
                (isBetween(minX, x4, maxX) && isBetween(minY, y4, maxY))) {
                System.out.println(1);

                printStraightLineOptional(x1, y1, x2, y2, x3, y3, x4, y4);
                
            } else {
                minY = Math.min(y3, y4);
                maxY = Math.max(y3, y4);
                minX = Math.min(x3, x4);
                maxX = Math.max(x3, x4);

                if ((isBetween(minX, x1, maxX) && isBetween(minY, y1, maxY)) || 
                    (isBetween(minX, x2, maxX) && isBetween(minY, y2, maxY))) {
                    System.out.println(1);

                    printStraightLineOptional(x1, y1, x2, y2, x3, y3, x4, y4);
                    
                } else {
                    System.out.println(0);
                }
            }
        } else {
            System.out.println(0);
        }
    }
}