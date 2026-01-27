def solution(score):
    sums = [s[0] + s[1] for s in score]     
    sorted_sums = sorted(sums, reverse=True)

    answer = []
    for s in sums:
        rank = sorted_sums.index(s) + 1
        answer.append(rank)

    return answer
