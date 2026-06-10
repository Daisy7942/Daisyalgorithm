def solution(a, b):
    carry = 0
    answer = ""

    a = a[::-1]
    b = b[::-1]

    for i in range(max(len(a), len(b))):
        x = int(a[i]) if i < len(a) else 0
        y = int(b[i]) if i < len(b) else 0

        s = x + y + carry
        answer += str(s % 10)
        carry = s // 10

    if carry:
        answer += str(carry)

    return answer[::-1]