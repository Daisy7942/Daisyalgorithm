def solution(emergency):
    answer = []
    number = sorted(emergency, reverse=True)
    for i in emergency:
        rank = number.index(i) + 1
        answer.append(rank)
    return answer
