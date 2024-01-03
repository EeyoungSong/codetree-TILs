digit = list(map(int, list(input())))

def Two2Ten(digit):
    s = 0
    for i in range(len(digit)):
        s += digit[::-1][i] * (2**i)
    
    return s

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

num = Two2Ten(digit) * 17
Ten2Two(num)