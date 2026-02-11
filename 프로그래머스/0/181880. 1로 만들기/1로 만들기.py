def solution(num_list):
    count = 0
    
    for x in num_list:
        while x > 1:
            x //= 2
            count += 1
            
    return count
