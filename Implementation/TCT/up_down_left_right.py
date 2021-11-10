n = int(input())
plans = input().split()
x, y = 1, 1

move_types = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)


# for plan in plans:
#     if plan == "L":
#         if not y == 1:
#             y -= 1
#     elif plan == "R":
#         if not y == n:
#             y += 1
#     elif plan == "U":
#         if not x == 1:
#             x -= 1
#     elif plan == "D":
#         if not x == n:
#             x += 1
