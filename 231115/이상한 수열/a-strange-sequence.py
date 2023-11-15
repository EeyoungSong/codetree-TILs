def strange(arr, c, n):
    if c == n:
        return arr[c - 2]+arr[(c//3) - 1]
    arr.append(arr[c - 2]+arr[(c//3) - 1])
    #print(arr[c - 2]+arr[(c//3) - 1])
    #print(arr)
    return strange(arr, c+1, n)

n = int(input())
arr = [1, 2]
print(strange(arr, 3, n))