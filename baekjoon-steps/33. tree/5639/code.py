import sys;
sys.setrecursionlimit(100001)

from bisect import bisect_left

preorder = [int(line) for line in sys.stdin]
tree = {}
postorder = []

def traverse(start, end, idx):
    if start >= end:
        return
    

    mid_idx = bisect_left(preorder[start+1:end+1], preorder[start]) + start + 1
    
    if start + 1 <= mid_idx - 1:
        traverse(start+1, mid_idx - 1, idx * 2)
        postorder.append(preorder[start + 1])

    if mid_idx <= end and mid_idx < len(preorder):
        traverse(mid_idx, end, idx * 2 + 1)
        postorder.append(preorder[mid_idx])

traverse(0, len(preorder) - 1, 1)
postorder.append(preorder[0])
print(*postorder, sep='\n')

