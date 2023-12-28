def func(n):
    if n <= 0:
        return
    print("HelloWorld")
    func(n-1)

n = int(input())
func(n)