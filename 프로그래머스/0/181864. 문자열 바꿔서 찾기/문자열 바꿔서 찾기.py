def solution(myString, pat):
    answer = 0
    changed = ""
    for c in myString:
        if c == "A":
            changed += "B"
        else:
            changed += "A"
    answer = int(pat in changed)

    return answer

