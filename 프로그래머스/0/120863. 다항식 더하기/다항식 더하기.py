def solution(polynomial):
    terms = polynomial.split(" + ")
    
    x_sum = 0
    num_sum = 0
    
    for term in terms:
        if 'x' in term:
            # "x" 또는 "3x"
            if term == 'x':
                x_sum += 1
            else:
                x_sum += int(term.replace('x', ''))
        else:
            num_sum += int(term)
    
    result = []
    
    if x_sum != 0:
        if x_sum == 1:
            result.append("x")
        else:
            result.append(f"{x_sum}x")
    
    if num_sum != 0:
        result.append(str(num_sum))
    
    if not result:
        return "0"
    
    return " + ".join(result)
