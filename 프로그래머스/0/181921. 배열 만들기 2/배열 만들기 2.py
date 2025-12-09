def solution(l, r):
    answer = []

    for num in range(l, r + 1):
        s = str(num)
        if all(ch in ['0', '5'] for ch in s):
            answer.append(num)

    return answer if answer else [-1]
