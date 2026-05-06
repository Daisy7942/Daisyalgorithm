def solution(num_list):

    return sorted(num_list)[:5]



if __name__ == "__main__":
    num_list = [12, 4, 15, 46, 38, 1, 14]
    result = solution(num_list)
    print(result)