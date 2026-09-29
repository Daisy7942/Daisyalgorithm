def solution(num_list):
    answer = 1
    answer2 = 0
    for i in num_list:
        answer*=i
        answer2+=i
    if answer <answer2**2:
        return 1
    else:
        return 0