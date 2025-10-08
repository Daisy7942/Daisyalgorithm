def solution(array):
    dic = {}
    for i in array:
        if i in dic : 
            dic[i] += 1
        else :
            dic[i] = 1
 
    max_count = max(dic.values())

    mode_list = [k for k, v in dic.items() if v == max_count]

    if len(mode_list) > 1:
        return -1
    else:
        return mode_list[0]

            
            