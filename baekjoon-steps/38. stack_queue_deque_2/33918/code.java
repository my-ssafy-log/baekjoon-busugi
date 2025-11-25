import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
	static int[][] dp = new int[200][25001];
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] tokens = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int N = tokens[0];
        int M = tokens[1];
        int C = tokens[2];
        int D = tokens[3];

        int[] bTokens = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        for (int time = 0; time < N; time++) {
        	for (int temp = 1; temp <= M; temp++) {
        		dp[time][temp] = M - Math.abs(bTokens[time] - temp);
//        		System.out.print(String.valueOf(time) + "," + String.valueOf(temp) + ": " + String.valueOf(dp[time][temp]) + "\t");
        	}
//        	System.out.println();
        }
        for (int time = 1; time < N; time++) {
        	for (int pivot = 1; pivot <= C; pivot++) {
        		Deque<int[]> dq = new ArrayDeque<int[]>();  // 최대값 덱 {온도, best}
        		
//        		System.out.println("pivot: " + String.valueOf(pivot));
        		// 처음 pivot 값에 닿는 time-1 에 값들로 dq 초기화
        		for (int i = pivot; i <= pivot + D && i <= M; i += C) {
        			int best = dp[time-1][i];
        			while (!dq.isEmpty() && dq.getLast()[1] < best) {
        				dq.removeLast();
        			}
        			dq.addLast(new int[] {i, best});
        		}
        		
        		dp[time][pivot] += dq.getFirst()[1];
        		
//        		for (int[] elem : dq) {
//    				System.out.print("[" + elem[0] + ", " + elem[1] + "]");
//    			}
//    			System.out.println();
        		
        		for (int i = pivot + C; i <= M; i += C) {
        			if (dq.getFirst()[0] < i - D) {  // 범위를 벗어난 온도 값 제거
        				dq.removeFirst();
        			}
        			
        			// i + D 값 덱에 추가
        			if (i + D <= M) {
	        			int best = dp[time-1][i+D];
	        			while (!dq.isEmpty() && dq.getLast()[1] < best) {
	        				dq.removeLast();
	        			}
	        			dq.addLast(new int[] {i+D, best});
        			}
        			
        			dp[time][i] += dq.getFirst()[1];
        			
//        			for (int[] elem : dq) {
//        				System.out.print("[" + elem[0] + ", " + elem[1] + "]");
//        			}
//        			System.out.println();
        		}
        	}
        }
        	
    	int best = -1;
    	for (int temp = 1; temp <= M; temp++) {
    		best = Math.max(best, dp[N-1][temp]);
    	}
    	System.out.println(best);
    }
}