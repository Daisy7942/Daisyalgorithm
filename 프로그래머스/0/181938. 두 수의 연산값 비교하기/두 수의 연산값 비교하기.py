def solution(a, b):

    ab = int(str(a) + str(b))
    double = 2 * a * b
    

    if ab >= double:
        return ab
    else:
        return double
