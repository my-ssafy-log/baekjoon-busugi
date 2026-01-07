import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Collectors;
import java.lang.*;
import java.io.*;

class LSI {
    static boolean isIntersecting(Segment segment1, Segment segment2) {
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
            return true;
        } else if (S1 == 0 && S2 == 0 && S3 == 0 && S4 == 0) {  // 4개의 점이 일직선에 있다면
            long minY = Math.min(y1, y2);
            long maxY = Math.max(y1, y2);
            long minX = Math.min(x1, x2);
            long maxX = Math.max(x1, x2);

            if ((isBetween(minX, x3, maxX) && isBetween(minY, y3, maxY)) || 
                (isBetween(minX, x4, maxX) && isBetween(minY, y4, maxY))) {
                return true;
                
            } else {
                minY = Math.min(y3, y4);
                maxY = Math.max(y3, y4);
                minX = Math.min(x3, x4);
                maxX = Math.max(x3, x4);

                if ((isBetween(minX, x1, maxX) && isBetween(minY, y1, maxY)) || 
                    (isBetween(minX, x2, maxX) && isBetween(minY, y2, maxY))) {
                    return true;
                }
            }
        }

        return false;
    }
    
    private static long getCCW(long x1, long y1, long x2, long y2, long x3, long y3) {
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

class UnionFind {
    int size;
    int[] parents = new int[3001];
    
    UnionFind(int N) {
        size = N;
        parents = IntStream.rangeClosed(0, N).toArray();
    }
    
    int find(int x) {
        if (parents[x] != x) parents[x] = find(parents[x]);
        return parents[x];
    }
    
    void union(int a, int b) {
        int pa = find(a);
        int pb = find(b);

        if (pa < pb) {
            parents[pb] = pa;
        } else {
            parents[pa] = pb;
        }
    }
    
    int getParentSize() {
        Set<Integer> set = new HashSet();
        for (int i = 1; i <= size; i++) {
            set.add(find(i));
        }
        return set.size();
    }
    
    int getMaxGroupSize() {
        List<Integer> list = Arrays.stream(parents)
            .filter(s -> s != 0)
            .boxed()
            .collect(Collectors.toList());
        
        int[] counters = new int[size + 1];
        int maxGroupSize = 0;

        for (int group : list) {
            counters[group] += 1;
            maxGroupSize = Math.max(maxGroupSize, counters[group]);
        }
        return maxGroupSize;
        
    }
}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        int maxSize = 1;

        List<Segment> segments = new ArrayList();
        UnionFind uf = new UnionFind(N);
        
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            
            long x1 = Long.parseLong(st.nextToken()),
                y1 = Long.parseLong(st.nextToken()),
                x2 = Long.parseLong(st.nextToken()),
                y2 = Long.parseLong(st.nextToken());

            segments.add(new Segment(x1, y1, x2, y2));
        }
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                Segment segment1 = segments.get(i);
                Segment segment2 = segments.get(j);

                if (LSI.isIntersecting(segment1, segment2)) {
                    uf.union(i + 1, j + 1);
                }
            }
        }
        System.out.println(uf.getParentSize());
        System.out.println(uf.getMaxGroupSize());
    }
}