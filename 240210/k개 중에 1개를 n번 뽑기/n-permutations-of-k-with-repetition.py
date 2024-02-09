k, n = map(int, input().split())

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

answer = []
def choose(current_num):
    if current_num > n:
        print_answer()
        return 
    
    for i in range(1, k+1):    
        answer.append(i)
        choose(current_num+1)
        answer.pop()

    return

choose(1)