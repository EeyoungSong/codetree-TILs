def print_star(n):
    if n == 0:
        return
    print_star(n-1)
    print(n, end=" ")
    

def print_star2(n):
    if n == 0:
        return
    print(n, end=" ")
    print_star2(n - 1)

n = int(input())
print_star(n)
print()
print_star2(n)