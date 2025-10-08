def solution(n):
    i = 1  # 피자 판 수
    while True:
        if (6 * i) % n == 0:  # n명에게 정확히 나누어 떨어지면
            return i
        i += 1
