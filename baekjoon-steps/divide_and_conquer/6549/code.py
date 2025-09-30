import sys
def readline():
    return sys.stdin.readline().rstrip()

while True:
    N, *arr = list(map(int, readline().split()))

    if N == 0:
        break
    
    def get_mid_area(s, e, max_area):
        mid = (s + e) // 2
        to_left = mid
        to_right = mid
        height = arr[mid]
        while to_left > s and to_right < e:
            if arr[to_left - 1] > arr[to_right + 1]:
                to_left -= 1
                height = min(height, arr[to_left])
            else:
                to_right += 1
                height = min(height, arr[to_right])
            max_area = max(max_area, (to_right - to_left + 1) * height)
        while to_right < e:
            to_right += 1
            height = min(height, arr[to_right])
            max_area = max(max_area, (to_right - to_left + 1) * height)
    
        while to_left > s:
            to_left -= 1
            height = min(height, arr[to_left])
            max_area = max(max_area, (to_right - to_left + 1) * height)
        return max_area
    
    def get_area(s, e):
        # print(f"get_area({s}, {e})")
        if s == e:
            return arr[s]
    
        mid = (s + e) // 2
        
        left_area = get_area(s, mid)
        right_area = get_area(mid+1, e)
        max_area = max(left_area, right_area)
    
        max_area = get_mid_area(s, e, max_area)
        # print(f"get_area({s}, {e}) - max_area: {max_area}")
    
        return max_area
    
    print(get_area(0, N-1))