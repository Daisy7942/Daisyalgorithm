def solution(array, n):
    array.sort()  # 오름차순 정렬
    return min(array, key=lambda x: abs(x - n))
