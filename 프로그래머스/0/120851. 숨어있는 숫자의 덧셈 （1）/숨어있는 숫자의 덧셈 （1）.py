def solution(my_string):
    answer = 0

    for ch in my_string:
        if ch in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            answer += int(ch)

    return answer