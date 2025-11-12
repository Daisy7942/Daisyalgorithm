def solution(order):
    count = 0
    for ch in str(order):
        if ch in ['3', '6', '9']:
            count += 1
    return count
