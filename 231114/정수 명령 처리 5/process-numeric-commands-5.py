n = int(input())
arr = []
for _ in range(n):
    c_arr = input().split()
    command = c_arr[0]
    if len(c_arr) == 2:
        if command == 'push_back':
            arr.append(c_arr[1])
        elif command == 'get':
            print(arr[int(c_arr[1])-1])
    elif len(c_arr) == 1:
        if command == 'size':
            print(len(arr))
        elif command == 'pop_back':
            arr.pop()