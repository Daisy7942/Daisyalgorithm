def solution(n, k):
    service = 0
    if n / 10 >= 1 :
        service += n//10
    price1 = 12000*n
    price2 = 2000*k - 2000*service
    answer = price1 + price2

    return answer