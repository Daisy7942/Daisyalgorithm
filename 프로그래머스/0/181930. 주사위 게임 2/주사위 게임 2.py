def solution(a, b, c):
    total = a + b + c
    total_sq = a**2 + b**2 + c**2
    total_cube = a**3 + b**3 + c**3

    if a == b == c:  
        return total * total_sq * total_cube
    elif a == b or a == c or b == c:
        return total * total_sq
    else:
        return total
