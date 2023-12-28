n = int(input())
arr = list(map(int, input().split()))

def get_max(arr, n, max_num):
    if n <= 0:
        return max(arr[n], max_num)
    return get_max(arr, n-1, max(arr[n], max_num))

print(get_max(arr, n-1, 0))