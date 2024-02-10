n = int(input())
arr = []
cnt = 0

def print_arr(arr):
    for elem in arr:
        print(elem, end=" ")
    print()

def choose(cnt):
    if len(arr) == n:
        cnt += 1
        #print_arr(arr)
    if len(arr) >= n:
        return cnt
    for i in range(1, 5):
        for j in range(i):
            arr.append(i)
        cnt = choose(cnt)
        for j in range(i):
            arr.pop()
    return cnt


print(choose(cnt))