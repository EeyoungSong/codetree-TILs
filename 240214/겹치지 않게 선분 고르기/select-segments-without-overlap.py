n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
answer = []
max_num = 0

def print_ans():
    for elem in answer:
        print(elem, end=" ")
    print()

def is_overlap():
    arr = [0] * 1001
    for elem in answer:
        a, b = lines[elem]
        for i in range(a, b+1):
            arr[i] += 1
    #print(arr)
    b = False
    for elem in arr:
        if elem >= 2:
            b = True
            break
    return b

    

def choose(curr_num, cnt, m):
    global max_num
    if curr_num >= n:
        if cnt == m:
            if not is_overlap():
                num = m
                max_num = max(max_num, num)
        return 

    answer.append(curr_num)
    choose(curr_num+1, cnt+1, m)
    answer.pop()

    choose(curr_num+1, cnt, m)

for m in range(n, 0, -1):
    choose(0, 0, m)

print(max_num)