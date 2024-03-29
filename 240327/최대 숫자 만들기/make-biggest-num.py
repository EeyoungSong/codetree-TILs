from functools import cmp_to_key


def compare(x, y):
    # x가 y보다 크다면
    # 우리가 원하는 방향입니다.
    if x + y > y + x:
        return -1
    # y가 x보다 크다면
    # 우리가 원하지 않는 방향입니다.
    if x + y > y + x:
        return 1
    # 우선 순위가 동일한 경우입니다.
    return 0


n = int(input())
arr = [input() for _ in range(n)]

# 내림차순 정렬
arr.sort(key=cmp_to_key(compare))

for elem in arr:
    print(elem, end="")