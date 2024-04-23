n = int(input())
building_arr = list(map(int, input().split()))
for i in range(2, n-2):
    a = building_arr[i-2]
    b = building_arr[i-1]
    c = building_arr[i+1]
    d = building_arr[i+2]
    m = max(a, b, c, d)
    print(m)