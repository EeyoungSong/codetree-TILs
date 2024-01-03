digit = list(map(int, list(input())))

def Two2Ten(digit):
    s = 0
    for i in range(len(digit)):
        s += digit[::-1][i] * (2**i)
    
    return s

print(Two2Ten(digit))