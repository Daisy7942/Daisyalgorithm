def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        temp = word

        for c in can:
            if temp.count(c) > 1:
                break
            temp = temp.replace(c, " ")


        if temp.replace(" ", "") == "":
            count += 1

    return count
