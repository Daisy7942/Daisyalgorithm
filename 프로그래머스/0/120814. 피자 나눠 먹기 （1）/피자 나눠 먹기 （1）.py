def solution(n):
    c = int(n / 7)
    if n % 7 != 0:
        c +=1

    return c