n, m, k = map(int, input().split())
turns = list(map(int, input().split()))
answer = []

def print_ans():
    for elem in answer:
        print(elem, end=" ")
    print()

def count_score():
    arr = [1] * (k+1)
    for x, d in zip(answer, turns):
        arr[x] += d
    
    score = 0
    for elem in arr:
        if elem >= m:
            score += 1
    #print(arr, score)
    return score 

def choose(curr_num, max_score):
    if curr_num > n:
        #print_ans()
        score = count_score()
        return max(score, max_score)
    
    for i in range(1, k+1):
        answer.append(i)
        max_score = choose(curr_num+1, max_score)
        answer.pop()
    
    return max_score

print(choose(1, 0))