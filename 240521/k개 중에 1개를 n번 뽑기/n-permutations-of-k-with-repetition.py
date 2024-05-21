k, n = map(int, input().split())
ans = []

def print_ans():
    for elem in ans:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num > n:
        print_ans()
        return
    
    for i in range(1, k+1):
        ans.append(i)
        choose(curr_num+1)
        ans.pop()
    
choose(1)