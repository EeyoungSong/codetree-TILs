n, k = map(int, input().split())
coin_list = sorted([int(input()) for _ in range(n)], reverse=True)
cnt = 0
r = 0

while True:
    if k <= 0:
        break
    coin = coin_list[r] 
    cnt += (k // coin)
    k -= coin * (k//coin)
    if r < len(coin_list):
        r += 1
    
print(cnt)