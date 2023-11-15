def strange(arr, c, n):
    if c == n:
        return arr[c - 2]+arr[(c//3) - 1]
    arr.append(arr[c - 2]+arr[(c//3) - 1])
    #print(arr[c - 2]+arr[(c//3) - 1])
    #print(arr)
    return strange(arr, c+1, n)

n = int(input())
arr = [1, 2]
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[1])
else:
    print(strange(arr, 3, n))