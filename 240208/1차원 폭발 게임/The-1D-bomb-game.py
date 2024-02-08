n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def boom(arr):
    boomed = False
    p = arr[0]
    cnt = 1
    indexs = []
    for i in range(1, len(arr)):
        if p == arr[i]:
            cnt += 1
            indexs.append(i)  
        else:
            cnt = 1
            indexs = []
        p = arr[i]
        if cnt >= m:
            for j in range(indexs[0]-1, indexs[-1]+1):
                arr[j] = 0
            boomed = True
    return arr, boomed

def remove_zero(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])
    
    return temp


while True:
    arr, boomed = boom(arr)
    if boomed == False:
        print(len(arr))
        for elem in arr:
            print(elem)
        break
    arr = remove_zero(arr)