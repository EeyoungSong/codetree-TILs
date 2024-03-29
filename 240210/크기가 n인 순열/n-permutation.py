n = int(input())
visited = [0] * (n+1)
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return
    
    for i in range(1, n+1):
        if visited[i] == 0:
            answer.append(i)
            visited[i] = 1
            choose(curr_num+1)
            answer.pop()
            visited[i] = 0

choose(1)