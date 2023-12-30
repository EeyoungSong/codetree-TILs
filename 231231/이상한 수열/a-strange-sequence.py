n = int(input())

def strange_seq(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return strange_seq(n//3) + strange_seq(n-1)

print(strange_seq(n))