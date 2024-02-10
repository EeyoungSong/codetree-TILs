MAX_NUM = 1000
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
answer = []


def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def check_overlap():
    arr = [0] * (MAX_NUM + 1)
    b = True
    for i in answer:
        a, b = lines[i]
        for j in range(a, b+1):
            arr[j] += 1
            if arr[j] >= 2:
                b = False
    return b
    
    
ans = -1
def choose(current_num, cnt, m):
    global ans
    if current_num >= n:
        if cnt == m:
            if check_overlap():
                ans = max(ans, cnt)
        return 
    
    answer.append(current_num)
    choose(current_num+1, cnt+1, m)
    answer.pop()

    choose(current_num+1, cnt, m)
    




for m in range(n, -1, -1):
    choose(0, 0, m)

print(ans)