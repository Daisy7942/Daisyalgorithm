def solution(money):
    answer = []
    if money >= 5500:
        answer.append(money // 5500)          # 살 수 있는 커피 잔 수
        answer.append(money % 5500)           # 남는 잔돈
    else:
        answer = [0, money]                   # 커피 못 사면 잔돈 그대로
    return answer