n, m = map(int, input().split())
c_list = []

def print_ans():
    for i in range(n):
        if c_list[i] == 1:
            print(i+1, end=" ")
    print()

def choose(curr_num, cnt):
    if curr_num > n:
        if cnt == m:
            print_ans()
        return
    
    c_list.append(1)
    choose(curr_num+1, cnt+1)
    c_list.pop()

    c_list.append(0)
    choose(curr_num+1, cnt)
    c_list.pop()
    
choose(1, 0)