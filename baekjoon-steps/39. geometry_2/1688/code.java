import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Collectors;
import java.lang.*;
import java.io.*;

enum LSIState {
    INTERSECT_POINT,
    RIGHT_T_LEFT_1,
    RIGHT_T_LEFT_2,
    INTERSECT_STRAIGHT,
    NOT_INTERSECT;
}

class LSI {
    static LSIState getIntersectState(Segment segment1, Segment segment2) {
        long x1 = segment1.x1, 
            y1 = segment1.y1, 
            x2 = segment1.x2, 
            y2 = segment1.y2, 
            x3 = segment2.x1, 
            y3 = segment2.y1, 
            x4 = segment2.x2, 
            y4 = segment2.y2;
        
        long S1 = getCCW(x1, y1, x2, y2, x3, y3);
        long S2 = getCCW(x1, y1, x2, y2, x4, y4);
        long S3 = getCCW(x3, y3, x4, y4, x1, y1);
        long S4 = getCCW(x3, y3, x4, y4, x2, y2);
        
        if (isOK(S1, S2) && isOK(S3, S4)) {
            // 만약 segment2의 꼭짓점이 segment1 선분 위에 있다면
            if (((S1 == 0 && S2 != 0) || (S1 != 0 && S2 == 0)) && S3 != 0 && S4 != 0) {

                // x3, y3이 겹친다면
                if (S1 == 0) return LSIState.RIGHT_T_LEFT_1;
                // x4, y4가 겹친다면
                else if (S2 == 0) return LSIState.RIGHT_T_LEFT_2;
            }
            
            return LSIState.INTERSECT_POINT;
        } else if (S1 == 0 && S2 == 0 && S3 == 0 && S4 == 0) {  // 4개의 점이 일직선에 있다면
            long minY = Math.min(y1, y2);
            long maxY = Math.max(y1, y2);
            long minX = Math.min(x1, x2);
            long maxX = Math.max(x1, x2);

            if ((isBetween(minX, x3, maxX) && isBetween(minY, y3, maxY)) || 
                (isBetween(minX, x4, maxX) && isBetween(minY, y4, maxY))) {
                return LSIState.INTERSECT_STRAIGHT;
                
            } else {
                minY = Math.min(y3, y4);
                maxY = Math.max(y3, y4);
                minX = Math.min(x3, x4);
                maxX = Math.max(x3, x4);

                if ((isBetween(minX, x1, maxX) && isBetween(minY, y1, maxY)) || 
                    (isBetween(minX, x2, maxX) && isBetween(minY, y2, maxY))) {
                    return LSIState.INTERSECT_STRAIGHT;
                }
            }
        }

        return LSIState.NOT_INTERSECT;
    }
    
    static long getCCW(long x1, long y1, long x2, long y2, long x3, long y3) {
        return x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3;
    }

    private static boolean isOK(long S1, long S2) {
        return (S1 == 0 && S2 != 0) || 
            (S1 != 0 && S2 == 0) || 
            (S1 < 0 && S2 > 0) || 
            (S1 > 0 && S2 < 0);
    }

    private static boolean isBetween(long a, long b, long c) {
        return a <= b && b <= c;
    }

    private static boolean isSameSign(long a, long b) {
        return (a < 0 && b < 0) || (a > 0 && b > 0) || (a == 0 && b == 0);
    }
}

class Segment {
    long x1, y1, x2, y2;
    Segment(long x1, long y1, long x2, long y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }
}

// The main method must be in a class named "Main".
class Main {
    static boolean isOnSegment(Segment segment, long x, long y) {
        long ccw = LSI.getCCW(segment.x1, segment.y1, segment.x2, segment.y2, x, y);
        long minY = Math.min(segment.y1, segment.y2),
            maxY = Math.max(segment.y1, segment.y2),
            minX = Math.min(segment.x1, segment.x2),
            maxX = Math.max(segment.x1, segment.x2);

        // System.out.println(String.format("%d, %d, %d, %d, %d, %d", segment.x1, segment.y1, segment.x2, segment.y2, x, y));
        // System.out.println(String.format("CCW: %d", ccw));
        // System.out.println(lsiState);

        return ccw == 0 && (minY <= y && y <= maxY && minX <= x && x <= maxX);
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        List<Segment> segmentList = new ArrayList();

        // 초기 점 설정
        st = new StringTokenizer(br.readLine());
        long x1 = Long.parseLong(st.nextToken()), 
            y1 = Long.parseLong(st.nextToken());

        for (int i = 1; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            long x2 = Long.parseLong(st.nextToken()), 
                y2 = Long.parseLong(st.nextToken());
            segmentList.add(new Segment(x1, y1, x2, y2));
            x1 = x2;
            y1 = y2;
        }
        
        segmentList.add(
            new Segment(x1, y1, segmentList.get(0).x1, segmentList.get(0).y1)
        );  // 끝점과 첫점 선분 추가

        int segmentListSize = segmentList.size();

        for (int i = 0; i < 3; i++) {
            int intersectPointCount = 0;
            
            st = new StringTokenizer(br.readLine());
            long x = Long.parseLong(st.nextToken()),
                y = Long.parseLong(st.nextToken());
            long xRay = 1000000001,
                yRay = y;

            Segment mySegment = new Segment(x, y, xRay, yRay);

            for (int j = 0; j < segmentListSize; j++) {
                Segment segment = segmentList.get(j);

                LSIState lsiState = LSI.getIntersectState(mySegment, segment);


                // 만약 선분 위에 점이 위치한다면
                // System.out.println(String.format("%d, %d, %d, %d, %d, %d", segment.x1, segment.y1, segment.x2, segment.y2, x, y));
                // System.out.println(String.format("CCW: %d", ccw));
                // System.out.println(lsiState);

                if (isOnSegment(segment, x, y)) {
                    // intersectPointCount에 (다각형 내부에 점이 있는 것이므로) -1 넣고 for문 break
                    intersectPointCount = -1;
                    break;
                }
                

                // 만약 현재 선분의 두번째 꼭짓점이 ray 선분 위에 있다면
                if (lsiState == LSIState.RIGHT_T_LEFT_2) {
                    // 현재 선분과 다음 선분의 CCW 부호 확인

                    // 교차하지 않는 첫번째 점의 ccw 찾기
                    long curCCW = LSI.getCCW(x, y, xRay, yRay, segment.x1, segment.y1);
                    
                    // LSIState.INTERSECT_STRAIGHT가 아닌 RIGHT_T_LEFT_1인 다음 선분의 두번째 점의 ccw 찾기
                    Segment nextSegment;
                    LSIState nextLSIState;
                    do {
                        j++;
                        nextSegment = segmentList.get(j % segmentListSize);

                        if (isOnSegment(nextSegment, x, y)) {
                            intersectPointCount = -1;
                            break;
                        }
                        
                        nextLSIState = LSI.getIntersectState(mySegment, nextSegment);
                    } while (nextLSIState == LSIState.INTERSECT_STRAIGHT);

                    if (intersectPointCount == -1) break;

                    long nextCCW = LSI.getCCW(x, y, xRay, yRay, nextSegment.x2, nextSegment.y2);

                    // nextCCW가 이라면

                    // 만약 curCCW와 nextCCW의 부호가 반대라면 이건 하나의 교차하는 선분으로 볼 수 있음
                    if ((curCCW < 0 && nextCCW > 0) || (curCCW > 0 && nextCCW < 0)) {
                        intersectPointCount++;
                        // System.out.println("Test");
                    }
                    // 그렇지 않다면 교차하는 선분이 아니라므로 무시
                }
                else if (lsiState == LSIState.INTERSECT_POINT) intersectPointCount++;
            }
            
            // bw.write(String.format("count: %d\n", intersectPointCount));
            if (Math.abs(intersectPointCount % 2) == 1) {
                bw.write("1\n");
            } else {
                bw.write("0\n");
            }
        }

        bw.flush();
        bw.close();
    }
}
