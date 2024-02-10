n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * (n+1)
answer = []


def make_sum():
    s = 0
    for i in range(n):
        s += grid[i][answer[i]] 
    return s

def choose(curr_num, max_num):
    if curr_num == n:
        s = make_sum()
        max_num = max(s, max_num)
        return max_num
    
    for i in range(0, n):
        if visited[i] == 0:
            answer.append(i)
            visited[i] = 1
            max_num = choose(curr_num+1, max_num)
            answer.pop()
            visited[i] = 0
    return max_num

print(choose(0, 0))