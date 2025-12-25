def solution(my_string, indices):
    remove = set(indices)
    answer = ""
    for i, ch in enumerate(my_string):
        if i not in remove:
            answer += ch
    return answer
