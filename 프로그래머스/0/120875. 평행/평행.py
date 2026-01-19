def solution(dots):
    def is_parallel(a, b, c, d):
        x1, y1 = a
        x2, y2 = b
        x3, y3 = c
        x4, y4 = d
        
        return (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1)

    if is_parallel(dots[0], dots[1], dots[2], dots[3]):
        return 1
    if is_parallel(dots[0], dots[2], dots[1], dots[3]):
        return 1
    if is_parallel(dots[0], dots[3], dots[1], dots[2]):
        return 1
    
    return 0
