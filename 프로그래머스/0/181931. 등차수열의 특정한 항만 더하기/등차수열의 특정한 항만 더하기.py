def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        term = a + d * i   # i번째 항 계산 (1항이 a)
        if included[i]:
            answer += term
    return answer
