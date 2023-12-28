n = int(input())

def get_sum(n):
    if n <= 1:
        return 0
    
    if n % 2 == 0:
        return get_sum(n // 2) + 1
    else:
        return get_sum(n // 3) + 1

print(get_sum(n))