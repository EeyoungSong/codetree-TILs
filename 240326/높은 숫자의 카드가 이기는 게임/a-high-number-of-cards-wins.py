n = int(input())
b_arr = [int(input()) for _ in range(n)]
b_arr.sort()
a_arr = [x for x in list(range(1, 2*n + 1)) if x not in b_arr]
a_arr.sort()

point = 0
for b in b_arr:
    for a in a_arr:
        if b < a:
            point += 1
            a_arr.remove(a)
            break
print(point)