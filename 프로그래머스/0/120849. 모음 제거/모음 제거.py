def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i]!=('a'):
            if my_string[i]!=('e'):
                if my_string[i]!=('i'):
                    if my_string[i]!=('o'):
                        if my_string[i]!=('u'):
                            answer+=my_string[i]          
    return answer