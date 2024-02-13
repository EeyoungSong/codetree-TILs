n, m = map(int, input().split())
num_list = list(map(int, input().split()))
answer = []
max_ans = 0

def print_ans():
    for elem in answer:
        print(elem, end=" ")
    print()

def xor():
    ans = answer[0]
    for i in range(1, m):
        ans = ans ^ answer[i]
    return ans
        


def choose(curr_num, cnt):
    global max_ans
    if curr_num > n:
        if cnt == m:
            a = xor()
            max_ans = max(a, max_ans)
        return 
    
    answer.append(curr_num)
    choose(curr_num+1, cnt+1)
    answer.pop()

    choose(curr_num+1, cnt)

choose(1, 0)
print(max_ans)