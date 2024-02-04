# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# square = 3
# max_num = 0

# for i in range(n):
#     for j in range(n-(square-1)):
#         cnt = 0
#         for k in range(square):
#             if grid[i][j+k] == 1:
#                 cnt += 1
#         max_num = max(cnt, max_num)

# print(max_num)


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

square = 3
max_num = 0

for i in range(n-(square-1)):
    for j in range(n-(square-1)):
        cnt = 0
        for k in range(square):
            for l in range(square):
                if grid[i+k][j+l] == 1:
                    cnt += 1
        max_num = max(cnt, max_num)

print(max_num)