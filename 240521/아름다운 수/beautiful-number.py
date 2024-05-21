n = int(input())
ans = []

cnt = 0
def beautiful_number(curr_num):
    global cnt
    if curr_num >= n:
        if curr_num == n:
            cnt += 1
            # print(ans)
        return
    
    for i in range(1, 5):
        for j in range(i):
            ans.append(i)

        beautiful_number(curr_num+i)

        for j in range(i):
            ans.pop()

    return cnt

print(beautiful_number(0))