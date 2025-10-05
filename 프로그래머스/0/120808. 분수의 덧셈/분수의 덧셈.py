import math
def solution(numer1, denom1, numer2, denom2):

    numerator = numer1 * denom2 + numer2 * denom1
    # 통분 후 분모 계산
    denominator = denom1 * denom2
    
    # 최대공약수로 나누어 기약분수 만들기
    gcd = math.gcd(numerator, denominator)
    
    return [numerator // gcd, denominator // gcd]
