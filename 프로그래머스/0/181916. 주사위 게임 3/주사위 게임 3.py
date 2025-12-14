from collections import Counter

def solution(a, b, c, d):
    nums = [a, b, c, d]
    cnt = Counter(nums)

    if len(cnt) == 1:
        return 1111 * a

    if len(cnt) == 2:
        (p, cp), (q, cq) = cnt.items()
        return (10*p + q)**2 if cp == 3 else (10*q + p)**2 if cq == 3 else (p + q) * abs(p - q)

    if len(cnt) == 3:
        q, r = [k for k, v in cnt.items() if v == 1]
        return q * r

    return min(nums)
