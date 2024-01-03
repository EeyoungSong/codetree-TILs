a, b = map(int, input().split())
n = input()

def A2Ten(digit, a):
    s = 0
    for i in range(len(digit)):
        s += digit[::-1][i] * (a**i)
    
    return s

def Ten2B(n, b):
    digit = []

    while True:
        if n < b:
            digit.append(n)
            break
        digit.append(n%b)
        n //= b
    
    for d in digit[::-1]:
        print(d, end="")


Ten2B(A2Ten(list(map(int, list(n))), a), b)