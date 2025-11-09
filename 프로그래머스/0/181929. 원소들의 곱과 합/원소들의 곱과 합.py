def solution(num_list):
    total_sum = sum(num_list)
    total_prod = 1
    for num in num_list:
        total_prod *= num

    if total_prod < total_sum ** 2:
        return 1
    else:
        return 0
