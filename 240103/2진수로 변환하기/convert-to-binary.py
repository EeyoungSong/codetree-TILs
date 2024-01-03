n = int(input())

def Ten2Two(n):
    digit = []

    while True:
        if n < 2:
            digit.append(n)
            break
        digit.append(n%2)
        n //= 2
    
    for d in digit[::-1]:
        print(d, end="")

Ten2Two(n)