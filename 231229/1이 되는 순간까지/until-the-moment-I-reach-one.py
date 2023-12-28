n = int(input())

def get_sum(n, cnt):
    if n <= 1:
        return cnt
    if n % 2 == 0:
        n //= 2
    else:
        n //= 3
    cnt += 1
    return get_sum(n, cnt)

print(get_sum(n, 0))