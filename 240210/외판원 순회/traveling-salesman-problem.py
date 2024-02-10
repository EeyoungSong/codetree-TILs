n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * (n+1)
answer = []
MAX_NUM = 10000000000


def make_sum():
    s = grid[0][answer[0]]
    if s == 0:
        return MAX_NUM
    for i in range(1, len(answer)):
        if grid[answer[i-1]][answer[i]] == 0:
            return MAX_NUM
        s += grid[answer[i-1]][answer[i]]
    s += grid[answer[-1]][0]
    if grid[answer[-1]][0] == 0:
        return MAX_NUM
    #print(s)
    return s

def choose(curr_num, min_num):
    if curr_num == n-1:
        #print(answer)
        s = make_sum()
        min_num = min(s, min_num)
        return min_num
    
    for i in range(1, n):
        if visited[i] == 0:
            answer.append(i)
            visited[i] = 1
            min_num = choose(curr_num+1, min_num)
            answer.pop()
            visited[i] = 0
    return min_num

print(choose(0, MAX_NUM))