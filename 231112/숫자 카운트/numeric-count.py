# 입력
n = int(input())

def check(i, j, k, b_arr):
    c1 = 0
    c2 = 0
    if i in b_arr:
        if b_arr.index(i) == 0:
            c1 += 1
        else:
            c2 += 1
    if j in b_arr:
        if b_arr.index(j) == 1:
            c1 += 1
        else:
            c2 += 1
    if k in b_arr:
        if b_arr.index(k) == 2:
            c1 += 1
        else:
            c2 += 1
    return c1, c2



n_arr = {}
for _ in range(n):
    b, a1, a2 = tuple(map(int, input().split()))
    b_arr = list(map(int, list(str(b))))
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and j != k and k != i:
                    c1, c2 = check(i, j, k, b_arr)
                    if c1 == a1 and c2 == a2:
                        num = ''.join(list(map(str, [i, j, k])))
                        if num in n_arr:
                            n_arr[num] += 1
                        else:
                            n_arr[num] = 1


cnt = 0
for key in n_arr:
    if n_arr[key] == n:
        cnt += 1

print(cnt)