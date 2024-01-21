MAX_NUM = 1000000
n, m = map(int, input().split())
arr_a = ['a'] * MAX_NUM
arr_b = ['b'] * MAX_NUM

def record(n, arr):
    at = 0
    a_dis = 0
    for i in range(n):
        d, t = input().split()
        t = int(t)
        if d == 'L':
            for j in range(at, at + t):
                arr[j] = a_dis
                at += 1
                a_dis -= 1
        else:
            for j in range(at, at + t):
                arr[j] = a_dis
                at += 1
                a_dis += 1

    return arr

arr_a = record(n, arr_a)
arr_b = record(m, arr_b)

check = True
for i in range(MAX_NUM):
    if (i != 0) and (arr_a[i] == arr_b[i]):
        print(i)
        check = False
        break

if check == True:
    print(-1)