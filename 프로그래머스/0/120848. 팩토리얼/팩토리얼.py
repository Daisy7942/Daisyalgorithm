def solution(n):
    fact = 1  # 1!부터 시작
    i = 1
    while True:
        fact *= i
        if fact > n:
            return i - 1
        i += 1
