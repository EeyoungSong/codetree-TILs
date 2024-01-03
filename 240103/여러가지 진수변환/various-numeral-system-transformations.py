n, b = map(int, input().split())

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

Ten2B(n, b)