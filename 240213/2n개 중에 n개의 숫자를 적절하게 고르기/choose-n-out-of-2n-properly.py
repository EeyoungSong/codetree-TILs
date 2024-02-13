import sys

n = int(input())
num_list = list(map(int, input().split()))
answer = []
min_ans = sys.maxsize

def print_ans():
    for elem in answer:
        print(elem, end=" ")
    print()

def get_diff():
    g1 = []
    g2 = []
    for i in range(2 * n):
        t = answer[i]
        if t == 0:
            g1.append(num_list[i])
        else:
            g2.append(num_list[i])
    
    return abs(sum(g1)-sum(g2))
        

def choose(curr_num, cnt):
    global min_ans
    if curr_num > 2 * n:
        if cnt == n:
            diff = get_diff()
            min_ans = min(min_ans, diff)
        return 
    
    answer.append(1)
    choose(curr_num+1, cnt+1)
    answer.pop()

    answer.append(0)
    choose(curr_num+1, cnt)
    answer.pop()

choose(1, 0)
print(min_ans)