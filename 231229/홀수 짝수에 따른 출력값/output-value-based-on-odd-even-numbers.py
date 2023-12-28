n = int(input())

def get_odd_sum(n):
    if n <= 0:
        return 0
    if n % 2 != 0:
        return get_odd_sum(n-1) + n
    else:
        return get_odd_sum(n-1) + 0

def get_even_sum(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return get_even_sum(n-1) + n
    else:
        return get_even_sum(n-1) + 0

if n % 2 == 0:
    print(get_even_sum(n))
else:
    print(get_odd_sum(n))