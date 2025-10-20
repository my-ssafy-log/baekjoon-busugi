import sys;
sys.setrecursionlimit(100001)

def get_preorder(postorder, inorder):
    inorder_map = {v: i for i, v in enumerate(inorder)}
    
    preorder = []
    
    def traverse(post_start, post_end, in_start, in_end):
        if post_start > post_end:
            return
        root_val = postorder[post_end]
        preorder.append(root_val)
        root_idx = inorder_map[root_val]
        left_size = root_idx - in_start

        traverse(post_start, post_start + left_size - 1, in_start, root_idx - 1)
        traverse(post_start + left_size, post_end - 1, root_idx + 1, in_end)
    
    traverse(0, len(postorder) - 1, 0, len(inorder) - 1)
    return preorder

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
print(*get_preorder(postorder, inorder))
