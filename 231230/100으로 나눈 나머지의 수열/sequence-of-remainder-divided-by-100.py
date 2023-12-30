n = int(input())

def get_n(n):
    if n == 1: 
        return 2
    elif n == 2:
        return 4
    return (get_n(n-1) * get_n(n-2)) % 100

print(get_n(n))