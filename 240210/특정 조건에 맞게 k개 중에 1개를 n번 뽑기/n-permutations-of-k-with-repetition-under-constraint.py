# n = 3
# answer = []

# def print_ans():
#     for elem in answer:
#         print(elem, end=" ")
#     print()

# def choose(curr_num):
#     if curr_num >= n + 1:
#         print_ans()
#         return
    
#     for i in range(2):
#         if i == 0 and answer != [] and answer[-1] == 0:
#             continue
#         answer.append(i)
#         choose(curr_num+1)
#         answer.pop()

#     # if curr_num == 1 or answer[-1] != 0:
#     #     answer.append(0)
#     #     choose(curr_num + 1)
#     #     answer.pop()
#     # answer.append(1)
#     # choose(curr_num+1)
#     # answer.pop()
    
# choose(1)

k, n = map(int, input().split())
answer = []

def print_ans():
    for elem in answer:
        print(elem, end=" ")
    print() 

def choose(curr_num, cnt):
    if curr_num > n:
        print_ans()
        return
    for i in range(1, k+1):
        if len(answer) >= 2 and answer[-1] == i and answer[-2] == i:
            continue
        answer.append(i)
        choose(curr_num+1, cnt)
        answer.pop()

choose(1, 0)