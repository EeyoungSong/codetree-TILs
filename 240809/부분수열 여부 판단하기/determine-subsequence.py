n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans_arr = []

i, j = 0, 0
while i < n and j < m:

    if arr1[i] < arr2[j]:
        ans_arr.append(arr1[i])
        i += 1
    else:
        ans_arr.append(arr2[j])
        j += 1

    
if i == n:
    for x in range(j, m):
        ans_arr.append(arr2[x])
elif j == m:
    for y in range(i, n):
        ans_arr.append(arr1[y])

print(ans_arr)