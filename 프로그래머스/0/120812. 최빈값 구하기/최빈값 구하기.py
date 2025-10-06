def solution(array):
    dic = {}
    for i in array:
        if i in dic : 
            dic[i] += 1
        else :
            dic[i] = 1
 
 # 2️⃣ 가장 큰 등장 횟수 찾기
    max_count = max(dic.values())

    # 3️⃣ max_count를 가진 숫자들 모으기
    mode_list = [k for k, v in dic.items() if v == max_count]

    # 4️⃣ 최빈값이 여러 개면 -1, 아니면 그 값 반환
    if len(mode_list) > 1:
        return -1
    else:
        return mode_list[0]

            
            