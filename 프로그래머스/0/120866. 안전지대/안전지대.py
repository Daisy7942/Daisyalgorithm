def solution(board):
    n = len(board)
    
    danger = [[False] * n for _ in range(n)]

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),  (0, 0),  (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        danger[ni][nj] = True

    count = 0
    for i in range(n):
        for j in range(n):
            if not danger[i][j]:
                count += 1
    
    return count
