from time import time

#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

#제출 시 solution.py 부분만 변경하여 제출해 주세요.

#####solution.py
#####solution.py
import heapq
from collections import defaultdict
from pprint import pprint

class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance

SIZE = None
TAXI_NUMBER = None
LEN = None
taxis = []
cnt = 0
buckets = []

def get_key(x, y):
    return x//LEN, y//LEN
def get_dist(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

def init(N, M, L, mXs, mYs):
    global SIZE, TAXI_NUMBER, LEN, taxis, buckets

    SIZE = N
    TAXI_NUMBER = M
    LEN = L
    taxis = [None] * M
    buckets = defaultdict(set)

    for i in range(M):
        x, y = mXs[i], mYs[i]
        taxi = {
            'no': i,
            'dist': [0, 0],
            'pos': (x, y)
        }
        taxis[i] = taxi
        buckets[get_key(x, y)].add(i)
    # pprint(buckets)

def pickup(mSX, mSY, mEX, mEY):
    global buckets
    m_key = get_key(mSX, mSY)

    best_no = None
    best_dist = float('inf')
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            nx, ny = m_key[0]+dx, m_key[1]+dy
            if not (0 <= nx < 10 and 0 <= ny < 10): continue

            for no in buckets[(nx, ny)]:
                dist = get_dist(taxis[no]['pos'], (mSX, mSY))
                if dist > LEN:
                    continue
                if best_dist > dist:
                    best_dist = dist
                    best_no = no
                elif best_dist == dist:
                    best_no = min(best_no, no)
    # pprint(get_key(mSX, mSY))
    # print(best_no)
    if best_no is not None:
        pos = taxis[best_no]['pos']
        taxis[best_no]['dist'][0] += get_dist(pos, (mSX, mSY)) + get_dist((mSX, mSY), (mEX, mEY))
        taxis[best_no]['dist'][1] += get_dist((mSX, mSY), (mEX, mEY))
        buckets[get_key(*pos)].remove(best_no)
        buckets[get_key(mEX, mEY)].add(best_no)
        taxis[best_no]['pos'] = (mEX, mEY)

        return best_no+1
    return -1

def reset(mNo):
    mx, my = taxis[mNo-1]['pos']
    move, ride = taxis[mNo-1]['dist']
    taxis[mNo-1]['dist'] = [0, 0]
    return Result(mx, my, move, ride)

def getBest(mNos):
    top5 = heapq.nlargest(5, taxis, key=lambda x: (x['dist'][1], -x['no']))

    for i, taxi in enumerate(top5):
        mNos[i] = taxi['no']+1
        # print(taxi['no']+1, end=' ')
    # print()

#####main.py
import sys
#from solution import init, pickup, reset, getBest

CMD_INIT = 100
CMD_PICKUP = 200
CMD_RESET = 300
CMD_GET_BEST = 400

MAX_M = 2000

mSeed = 0
def pseudo_rand():
	global mSeed
	mSeed = (mSeed * 1103515245 + 12345) % 2147483647
	return mSeed >> 16


mXs = [0 for _ in range(MAX_M)]
mYs = [0 for _ in range(MAX_M)]

def run1():
	global mSeed

	mNos = [0] * 5

	Q, mSeed = map(int, input().split())
	okay = False

	for q in range(Q):
		input_iter = iter(input().split())
		cmd = int(next(input_iter))
		if cmd == CMD_INIT:
			N = int(next(input_iter))
			M = int(next(input_iter))
			L = N // 10
			for i in range(M):
				mXs[i] = pseudo_rand() % N
				mYs[i] = pseudo_rand() % N
			init(N, M, L, mXs, mYs)
			okay = True
		elif cmd == CMD_PICKUP:
			while True:
				mSX = pseudo_rand() % N
				mSY = pseudo_rand() % N
				mEX = pseudo_rand() % N
				mEY = pseudo_rand() % N
				if mSX != mEX or mSY != mEY:
					break
			ret = pickup(mSX, mSY, mEX, mEY)
			ans = int(next(input_iter))
			if ret != ans:
				okay = False
		elif cmd == CMD_RESET:
			mNo = int(next(input_iter))
			res = reset(mNo)
			x = int(next(input_iter))
			y = int(next(input_iter))
			mdist = int(next(input_iter))
			rdist = int(next(input_iter))
			if res.mX != x or res.mY != y or res.mMoveDistance != mdist or res.mRideDistance != rdist:
				okay = False
		elif cmd == CMD_GET_BEST:
			getBest(mNos)
			for i in range(5):
				ans = int(next(input_iter))
				if mNos[i] != ans:
					okay = False
		else:
			okay = False
	return okay


sys.stdin = open('sample_input.txt', 'r')

T, MARK = map(int, input().split())

st = time()
for tc in range(1, T + 1):
	score = MARK if run1() else 0
	print("#%d %d" % (tc, score))
et = time()
print(et - st)