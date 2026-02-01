def solution(i, j, k):
    s = ''.join(str(x) for x in range(i, j+1))
    return s.count(str(k))
