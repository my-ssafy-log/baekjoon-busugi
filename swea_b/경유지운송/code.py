#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

#제출 시 solution.py 부분만 변경하여 제출해 주세요.

#####solution.py
import heapq

INF = int(1e9)

N = None
K = None
graph = []
def init(n, k, sCity, eCity, mLimit):
    global N, K, graph
    N = n
    K = k
    graph = [[] for _ in range(N)]

    for i in range(K):
        u, v, limit = sCity[i], eCity[i], mLimit[i]
        graph[u].append((v, limit))
        graph[v].append((u, limit))

def add(sCity, eCity, mLimit):
    graph[sCity].append((eCity, mLimit))
    graph[eCity].append((sCity, mLimit))

def calculate(sCity, eCity, M, mStopover):
    completed = set()
    completed.add(sCity)
    stopoverset = set(mStopover)
    stopoverset.add(sCity)
    stopoverset.add(eCity)
    hq = []
    d = [0] * N
    d[sCity] = INF


    for nbr, limit in graph[sCity]:
        d[nbr] = limit
        heapq.heappush(hq, (-limit, nbr))


    while hq and len(stopoverset - completed) > 0:
        limit, cur = heapq.heappop(hq)
        limit = -limit
        if d[cur] > limit: continue

        for nbr, nlimit in graph[cur]:
            if d[nbr] < min(nlimit, d[cur]):
                if nbr in completed:
                    completed.remove(nbr)
                d[nbr] = min(nlimit, d[cur])
                heapq.heappush(hq, (-d[nbr], nbr))
        completed.add(cur)

    if len(stopoverset - completed) > 0:
        return -1

    best = INF
    for stopover in stopoverset:
        best = min(best, d[stopover])

    return best


#####main.py
import sys

#from solution import init, add, calculate

CMD_INIT = 100
CMD_ADD = 200
CMD_CALC = 300

def run1():
	q = int(input())
	okay = False

	sCityArr = []
	eCityArr = []
	mLimitArr = []

	for i in range(q):
		cmd = int(input().split()[0])

		if cmd == CMD_INIT:
			inputarray = input().split()
			n = int(inputarray[1])
			k = int(inputarray[3])
			for _ in range(k):
				road = input().split()
				sCityArr.append(int(road[1]))
				eCityArr.append(int(road[3]))
				mLimitArr.append(int(road[5]))

			init(n, k, sCityArr, eCityArr, mLimitArr)
			okay = True
		elif cmd == CMD_ADD:
			inputarray = input().split()
			sCity = int(inputarray[1])
			eCity = int(inputarray[3])
			mLimit = int(inputarray[5])
			add(sCity, eCity, mLimit)
		elif cmd == CMD_CALC:
			inputarray = input().split()
			sCity = int(inputarray[1])
			eCity = int(inputarray[3])
			m = int(inputarray[5])
			mStopover = []
			for _ in range(m):
				mStopover.append(int(input().split()[1]))

			ans = int(input().split()[1])
			ret = calculate(sCity, eCity, m, mStopover)
			if ans != ret:
				okay = False
		else:
			okay = False

	return okay


if __name__ == '__main__':
	sys.stdin = open('sample_input.txt', 'r')
	inputarray = input().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, TC + 1):
		score = MARK if run1() else 0
		print("#%d %d" % (testcase, score), flush = True)