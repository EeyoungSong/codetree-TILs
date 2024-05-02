n = int(input())
all_arr = [i for i in range(1, 2*n+1)]
b_arr = [int(input()) for _ in range(n)]
a_arr = list(set(all_arr) - set(b_arr))

def can_win(num): # 들어온 숫자를 a_arr의 숫자가 이길 수 있는지 검사
    can_win_arr = []
    for a in a_arr:
        if a >= num:
            can_win_arr.append(a)
            return can_win_arr
    return False

ans = 0
for b in b_arr:
    can_win_arr = can_win(b)
    if can_win_arr:
        a_arr.remove(min(can_win_arr))
        ans += 1
    else:
        a_arr.remove(min(a_arr))

print(ans)