n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

t = arr[0]
for elem in arr[1:]:
    lcm = t * elem // gcd(t, elem)
    t = lcm
print(t)