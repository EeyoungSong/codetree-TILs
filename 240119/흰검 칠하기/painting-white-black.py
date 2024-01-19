offset = 100000
MAX_NUM = 200000
n = int(input())
check_arr = [[0, 0] for _ in range(MAX_NUM + 1)]
color_arr = ['' for _ in range(MAX_NUM + 1)] 
p = 0

def color_tiles(x, p, d):
    if d == 'L':
        for i in range(p, p-x, -1):
            if color_arr[i + offset] != 'g':
                color_arr[i + offset] = 'w'
                check_arr[i + offset][0] += 1 
                if check_grey(i + offset):
                    color_arr[i + offset] = 'g'
            
        return p - x + 1


    elif d == 'R':
        for i in range(p, p+x):
            if color_arr[i + offset] != 'g':
                color_arr[i + offset] = 'b'
                check_arr[i + offset][1] += 1
                if check_grey(i + offset):
                    color_arr[i + offset] = 'g'
                
        return p + x - 1

def check_grey(i):
    if check_arr[i][0] >= 2 and check_arr[i][1] >= 2:
        return True

for _ in range(n):
    x, d = input().split()
    x = int(x)
    p = color_tiles(x, p, d)


print(color_arr.count('w'), color_arr.count('b'), color_arr.count('g'))