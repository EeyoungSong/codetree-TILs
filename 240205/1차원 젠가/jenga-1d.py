n = int(input())
arr = [int(input()) for _ in range(n)]


for i in range(2):
    temp = []
    a, b = map(int, input().split())
    for i in range(len(arr)):
        if a-1 <= i < b:
            arr[i] = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])
    arr = temp 
   # print(arr)
print(len(arr))
for elem in arr:
    print(elem)