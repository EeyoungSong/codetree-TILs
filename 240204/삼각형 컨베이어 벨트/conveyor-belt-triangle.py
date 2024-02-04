n, t = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))

def move_num(l1, l2, l3):
    lst = l1 + l2 + l3
    temp = lst[-1]
    n = len(lst)
    for i in range(n-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = temp
    return lst[:n//3], lst[n//3:(n//3)*2], lst[(n//3)*2:]


for _ in range(t):
    l1, l2, l3 = move_num(l1, l2, l3)

for elem in l1:
    print(elem, end=" ")
print()
for elem in l2:
    print(elem, end=" ")    
print()
for elem in l3:
    print(elem, end=" ")