a, b, c = map(int, input().split())
n = a * b * c

def calc(n):
    if n < 10:
        return n
    return calc(n // 10) + (n % 10) 
    
print(calc(n))