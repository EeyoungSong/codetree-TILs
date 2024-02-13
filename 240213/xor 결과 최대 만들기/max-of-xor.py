n, m = map(int, input().split())
num_list = list(map(int, input().split()))
answer = []
max_ans = 0

def print_ans():
    for elem in answer:
        print(elem, end=" ")
    print()

def xor():
    answer_num = []
    for i in range(m):
        if answer[i] == 1:
            answer_num.append(num_list[i])
    ans = answer_num[0]
    for i in range(1, m):
        ans = ans ^ answer_num[i]
    return ans
        


def choose(curr_num, cnt):
    global max_ans
    if curr_num > n:
        if cnt == m:
            a = xor()
            max_ans = max(a, max_ans)
        return 
    
    answer.append(1)
    choose(curr_num+1, cnt+1)
    answer.pop()

    answer.append(0)
    choose(curr_num+1, cnt)
    answer.pop()

choose(1, 0)
print(max_ans)