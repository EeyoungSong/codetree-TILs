n, t = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

def move_num(l1, l2):
    lst = l1 + l2
    temp = lst[-1]
    n = len(lst)
    for i in range(n-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = temp
    return lst[:n//2], lst[n//2:]


for _ in range(t):
    l1, l2 = move_num(l1, l2)

for elem in l1:
    print(elem, end=" ")
print()
for elem in l2:
    print(elem, end=" ")