def get_pi(p):
    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(s, p):
    pos_list = []
    j = 0
    pi = get_pi(p)
    for i in range(0, len(s)):
        while j > 0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                pos_list.append(i-len(p)+1)
                j = pi[j]
            else:
                j += 1
    return pos_list

print(kmp("ABABABABBABABABABCBABABABABC", "ABABABABC"))