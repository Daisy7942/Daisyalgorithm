def solution(numbers, k):
    idx = 0
    for i in range(1, k) :
        idx = idx+2
        if idx >= len(numbers):
            idx = idx-len(numbers)    
            
    return numbers[idx]